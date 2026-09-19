"""
Extract API documentation from .agent-refs/APIDump/ Lua files and generate
markdown tiddlers in tiddlers/ for TiddlyWiki.
"""

import os
import re
import html2text
from pathlib import Path

from lupa import LuaRuntime

BASE = Path(__file__).parent
ROOT = BASE.parent
APIDUMP = ROOT / ".agent-refs" / "APIDump"
TIDDLERS = ROOT / "tiddlers"
STATIC = APIDUMP / "Static"
CLASSES_DIR = APIDUMP / "Classes"
HOOKS_DIR = APIDUMP / "Hooks"

# ── Lua helpers ──────────────────────────────────────────────────────────────

_lua = LuaRuntime(unpack_returned_tuples=True)


def load_lua_file(path):
    """Load a Lua file that returns a table, return the dict."""
    # lupa can't directly load 'return { ... }' files, so we wrap them
    code = path.read_text(encoding="utf-8")
    result = _lua.eval("(function() " + code + " end)()")
    return _table_to_dict(result)


# Get lupa LuaTable type once
from lupa import LuaRuntime
_LUA_RT = LuaRuntime(unpack_returned_tuples=True)
_LUA_TABLE_TYPE = type(_LUA_RT.eval('{}'))


def _table_to_dict(t):
    """Recursively convert a lupa LuaTable to plain Python dicts/lists."""

    def _convert(v):
        if v is None:
            return None
        if isinstance(v, _LUA_TABLE_TYPE):
            keys = list(v.keys())
            int_keys = [k for k in keys if isinstance(k, int)]
            if int_keys and max(int_keys) == len(int_keys):
                arr = []
                for i in range(1, len(int_keys) + 1):
                    arr.append(_convert(v[i]))
                return arr
            d = {}
            for k in keys:
                d[str(k)] = _convert(v[k])
            return d
        if isinstance(v, (int, float)):
            return v
        if isinstance(v, bytes):
            return v.decode("utf-8")
        if isinstance(v, str):
            return v
        return v

    return _convert(t)


# ── Markdown generation ──────────────────────────────────────────────────────

def clean_desc(text):
    """Clean description text: unwrap newlines, collapse whitespace."""
    if not text:
        return ""
    text = text.replace("</p>", "\n\n")
    text = text.replace("<p>", "")
    text = text.replace("<br>", "\n")
    text = text.replace("<br/>", "\n")
    text = text.replace("<br />", "\n")
    # Convert bullet lists
    text = re.sub(r"<ul>\s*<li>", "\n- ", text)
    text = text.replace("</li>", "")
    text = re.sub(r"</ul>\s*", "\n", text)
    text = re.sub(r"<ol>\s*<li>", "\n1. ", text)
    text = text.replace("</ol>", "\n")
    # Strip remaining HTML tags
    text = re.sub(r"<[^>]+>", "", text)
    # Collapse multiple blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = text.strip()
    return text


def convert_internal_links(text):
    """Convert {{ClassName}} and {{ClassName|Text}} to [Text](ClassName.md)"""
    text = re.sub(
        r"\{\{(c\w+)#(\w+)\}\}",
        r"[\1::\2](\1.md)",
        text,
    )
    text = re.sub(
        r"\{\{(c\w+)\|([^}]+)\}\}",
        r"[\2](\1.md)",
        text,
    )
    text = re.sub(
        r"\{\{(c\w+)\}\}",
        r"[\1](\1.md)",
        text,
    )
    return text


def type_to_md(t):
    """Format a type string."""
    # Handle references like cPluginManager#ePluginStatus
    t = re.sub(r"#(\w+)", r" \1", t)
    return t


def format_function_table(func_data):
    """Format a function (which may have multiple overloads) into a markdown table."""
    if not func_data:
        return ""
    overloads = func_data if isinstance(func_data, list) else [func_data]
    lines = []
    for ol in overloads:
        if not isinstance(ol, dict):
            continue
        params = ol.get("Params", []) or []
        returns = ol.get("Returns", []) or []
        notes = ol.get("Notes", "")
        is_static = ol.get("IsStatic", False)

        param_str = ", ".join(
            f"{p.get('Name', '?')}: {type_to_md(p.get('Type', '?'))}{'?' if p.get('IsOptional') else ''}" if isinstance(p, dict) else str(p)
            for p in params
        )
        return_str = ", ".join(
            f"{type_to_md(r.get('Type', '?'))}{' ' + r.get('Name', '') if r.get('Name') else ''}" if isinstance(r, dict) else str(r)
            for r in returns
        )
        prefix = "static " if is_static else ""
        notes_clean = clean_desc(notes) if notes else ""
        lines.append(f"| `{prefix}({param_str})` → `{return_str}` | {notes_clean} |")
    return "\n".join(lines)


def format_constants(constants):
    """Format constants table. Handles both dict and list formats."""
    if not constants:
        return ""
    lines = ["| Name | Value | Notes |", "|---|---|---|"]
    if isinstance(constants, dict):
        for name, info in sorted(constants.items()):
            if isinstance(info, dict):
                val = info.get("Value", "")
                notes = clean_desc(info.get("Notes", ""))
            else:
                val = str(info)
                notes = ""
            lines.append(f"| `{name}` | `{val}` | {notes} |")
    elif isinstance(constants, list):
        for item in constants:
            if isinstance(item, dict):
                name = item.get("Name", "?")
                val = item.get("Value", "")
                notes = clean_desc(item.get("Notes", ""))
                lines.append(f"| `{name}` | `{val}` | {notes} |")
    return "\n".join(lines)


def filter_constants_by_groups(all_constants, constant_groups):
    """Group constants as specified by ConstantGroups."""
    if not constant_groups or not all_constants:
        if all_constants:
            return {"": {"constants": all_constants, "text_before": "", "text_after": ""}}
        return {}

    groups = {}
    seen = set()

    for group_name, group_info in constant_groups.items():
        include_patterns = group_info.get("Include", [])
        group_consts = {}
        for name, val in all_constants.items():
            for pat in include_patterns:
                if re.match(pat.replace("*", ".*"), name):
                    group_consts[name] = val
                    seen.add(name)
                    break
        text_before = group_info.get("TextBefore", "")
        text_after = group_info.get("TextAfter", "")
        groups[group_name] = {
            "constants": group_consts,
            "text_before": text_before,
            "text_after": text_after,
        }

    # Any remaining constants
    remainder = {k: v for k, v in all_constants.items() if k not in seen}
    if remainder:
        groups[""] = {"constants": remainder, "text_before": "", "text_after": ""}

    return groups


def format_variables(variables):
    """Format member variables table."""
    if not variables:
        return ""
    lines = ["| Name | Type | Notes |", "|---|---|---|"]
    if isinstance(variables, dict):
        for name, info in sorted(variables.items()):
            if isinstance(info, dict):
                vtype = type_to_md(info.get("Type", "?"))
                notes = clean_desc(info.get("Notes", ""))
            else:
                vtype = "?"
                notes = clean_desc(str(info))
            lines.append(f"| `{name}` | `{vtype}` | {notes} |")
    return "\n".join(lines)


# ── Class tiddler generation ─────────────────────────────────────────────────

def generate_class_tiddler(class_name, class_data):
    """Generate a markdown tiddler for a class."""
    desc = clean_desc(class_data.get("Desc", ""))
    inherits = class_data.get("Inherits", None)
    functions = class_data.get("Functions", {}) or {}
    constants = class_data.get("Constants", {}) or {}
    constant_groups = class_data.get("ConstantGroups", {}) or {}
    variables = class_data.get("Variables", {}) or {}
    additional_info = class_data.get("AdditionalInfo", []) or []

    title = f"{class_name} (class)"
    
    md_parts = []

    # Description
    md_parts.append(f"# {class_name}")
    md_parts.append("")
    if inherits:
        md_parts.append(f"**Inherits:** [{inherits}]({inherits}.md)")
        md_parts.append("")
    md_parts.append(convert_internal_links(desc))
    md_parts.append("")

    # Functions
    if functions:
        md_parts.append("## Functions")
        md_parts.append("")
        for fname in sorted(functions.keys()):
            fdata = functions[fname]
            overloads = fdata if isinstance(fdata, list) else [fdata]
            is_static = any(
                isinstance(ol, dict) and ol.get("IsStatic")
                for ol in overloads
            )
            prefix = "static " if is_static else ""
            md_parts.append(f"### {prefix}{fname}")
            md_parts.append("")
            table = format_function_table(fdata)
            if table:
                md_parts.append(table)
                md_parts.append("")

    # Groups for constants
    if constants:
        grouped = filter_constants_by_groups(constants, constant_groups)
        for group_name, group_data in (grouped or {}).items():
            if group_name:
                md_parts.append(f"## Constants: {group_name}")
                md_parts.append("")
            else:
                md_parts.append("## Constants")
                md_parts.append("")
            tb = group_data.get("text_before", "")
            if tb:
                md_parts.append(convert_internal_links(clean_desc(tb)))
                md_parts.append("")
            md_parts.append(format_constants(group_data["constants"]))
            md_parts.append("")
            ta = group_data.get("text_after", "")
            if ta:
                md_parts.append(convert_internal_links(clean_desc(ta)))
                md_parts.append("")

    # Variables
    if variables:
        md_parts.append("## Member Variables")
        md_parts.append("")
        md_parts.append(format_variables(variables))
        md_parts.append("")

    # Additional info
    if additional_info:
        for section in additional_info:
            if isinstance(section, dict):
                header = section.get("Header", "")
                contents = section.get("Contents", "")
                if header:
                    md_parts.append(f"## {header}")
                    md_parts.append("")
                if contents:
                    md_parts.append(convert_internal_links(clean_desc(contents)))
                    md_parts.append("")

    content = "\n".join(md_parts).strip()
    return title, content


# ── Hook tiddler generation ──────────────────────────────────────────────────

def generate_hook_tiddler(hook_name, hook_data):
    """Generate a markdown tiddler for a hook."""
    called_when = hook_data.get("CalledWhen", "")
    default_fn = hook_data.get("DefaultFnName", "")
    desc = clean_desc(hook_data.get("Desc", ""))
    params = hook_data.get("Params", []) or []
    returns_text = hook_data.get("Returns", "")
    examples = hook_data.get("Examples", []) or []

    title = f"{default_fn} (hook)"

    md_parts = []
    md_parts.append(f"# {hook_name}: {default_fn}")
    md_parts.append("")
    md_parts.append(f"**Called when:** {called_when}")
    md_parts.append("")

    if desc:
        md_parts.append(convert_internal_links(desc))
        md_parts.append("")

    # Parameters
    if params:
        md_parts.append("## Parameters")
        md_parts.append("")
        md_parts.append("| Name | Type | Notes |")
        md_parts.append("|---|---|---|")
        for p in params:
            pname = p.get("Name", "?")
            ptype = type_to_md(p.get("Type", "?"))
            pnotes = p.get("Notes", "")
            md_parts.append(f"| `{pname}` | `{ptype}` | {pnotes} |")
        md_parts.append("")

    # Returns
    if returns_text:
        md_parts.append("## Return Value")
        md_parts.append("")
        md_parts.append(convert_internal_links(clean_desc(returns_text)))
        md_parts.append("")

    # Examples
    if examples:
        md_parts.append("## Examples")
        md_parts.append("")
        for ex in examples:
            if isinstance(ex, dict):
                ex_title = ex.get("Title", "Example")
                ex_desc = ex.get("Desc", "")
                ex_code = ex.get("Code", "")
                if ex_title:
                    md_parts.append(f"### {ex_title}")
                    md_parts.append("")
                if ex_desc:
                    md_parts.append(convert_internal_links(clean_desc(ex_desc)))
                    md_parts.append("")
                if ex_code:
                    md_parts.append(f"```lua")
                    md_parts.append(ex_code.strip())
                    md_parts.append("```")
                    md_parts.append("")

    content = "\n".join(md_parts).strip()
    return title, content


# ── Globals tiddler ─────────────────────────────────────────────────────────

def generate_globals_tiddler(globals_data):
    """Generate a globals markdown tiddler."""
    if not globals_data:
        return None, None
    desc = clean_desc(globals_data.get("Desc", ""))
    functions = globals_data.get("Functions", {}) or {}
    constants = globals_data.get("Constants", {}) or {}
    variables = globals_data.get("Variables", {}) or {}

    title = "Globals (class)"

    md_parts = ["# Globals", ""]
    if desc:
        md_parts.append(convert_internal_links(desc))
        md_parts.append("")

    # Functions
    if functions:
        md_parts.append("## Functions")
        md_parts.append("")
        for fname in sorted(functions.keys()):
            fdata = functions[fname]
            md_parts.append(f"### {fname}")
            md_parts.append("")
            table = format_function_table(fdata)
            if table:
                md_parts.append(table)
                md_parts.append("")

    # Constants
    if constants:
        md_parts.append("## Constants")
        md_parts.append("")
        md_parts.append(format_constants(constants))
        md_parts.append("")

    # Variables
    if variables:
        md_parts.append("## Variables")
        md_parts.append("")
        md_parts.append(format_variables(variables))
        md_parts.append("")

    content = "\n".join(md_parts).strip()
    return title, content


# ── Article tiddler generation ───────────────────────────────────────────────

def generate_article_tiddler(filename, title_text):
    """Convert an HTML article to markdown tiddler."""
    path = APIDUMP / filename
    if not path.exists():
        print(f"  [SKIP] Article file not found: {filename}")
        return None, None
    html = path.read_text(encoding="utf-8")
    h = html2text.HTML2Text()
    h.body_width = 0  # no wrapping
    h.ignore_links = False
    h.ignore_images = False
    h.ignore_emphasis = False
    md = h.handle(html)
    # Clean up
    md = convert_internal_links(md)
    # Remove the first line if it's a duplicate title
    lines = md.strip().split("\n")
    if lines and lines[0].startswith("# ") and title_text in lines[0]:
        lines = lines[1:]
    md = "\n".join(lines).strip()
    tiddler_title = f"{title_text} (article)"
    return tiddler_title, md


# ── Main extraction loop ──────────────────────────────────────────────────────

def main():
    TIDDLERS.mkdir(exist_ok=True)

    # ── 1. Load APIDesc.lua which may have additional class data ──
    print("Loading APIDesc.lua...")
    try:
        apidesc = load_lua_file(APIDUMP / "APIDesc.lua")
    except Exception as e:
        print(f"  [ERROR] Failed to load APIDesc.lua: {e}")
        apidesc = {}
    
    apidesc_classes = apidesc.get("Classes", {}) or {}
    apidesc_hooks = apidesc.get("Hooks", {}) or {}
    apidesc_globals = apidesc.get("Globals", {}) or {}

    # ── 2. Load individual class files ──
    class_data = dict(apidesc_classes)
    for f in sorted(CLASSES_DIR.glob("*.lua")):
        try:
            data = load_lua_file(f)
            class_data.update(data)
            print(f"  [OK] Class file: {f.name}")
        except Exception as e:
            print(f"  [ERR] Class file {f.name}: {e}")

    # ── 3. Load individual hook files ──
    hook_data = dict(apidesc_hooks)
    for f in sorted(HOOKS_DIR.glob("*.lua")):
        try:
            data = load_lua_file(f)
            hook_data.update(data)
            print(f"  [OK] Hook file: {f.name}")
        except Exception as e:
            print(f"  [ERR] Hook file {f.name}: {e}")

    # ── 4. Generate class tiddlers ──
    print("\n--- Generating Class Tiddlers ---")
    class_count = 0
    for cname in sorted(class_data.keys()):
        cd = class_data[cname]
        if not isinstance(cd, dict):
            continue
        try:
            title, content = generate_class_tiddler(cname, cd)
            if title and content:
                filename = re.sub(r"[^a-zA-Z0-9_-]", "_", cname) + ".md"
                path = TIDDLERS / filename
                tid = f"# {title}\n\n{content}\n"
                path.write_text(tid, encoding="utf-8")
                class_count += 1
        except Exception as e:
            import traceback
            print(f"  [ERR] {cname}: {e}")
            traceback.print_exc()

    # ── 5. Generate hook tiddlers ──
    print("\n--- Generating Hook Tiddlers ---")
    hook_count = 0
    for hname in sorted(hook_data.keys()):
        hd = hook_data[hname]
        if not isinstance(hd, dict):
            continue
        try:
            title, content = generate_hook_tiddler(hname, hd)
            if title and content:
                fn = hd.get("DefaultFnName", hname)
                filename = f"{fn}.md"
                path = TIDDLERS / filename
                tid = f"# {title}\n\n{content}\n"
                path.write_text(tid, encoding="utf-8")
                hook_count += 1
                print(f"  [OK] {hname} -> {filename}")
        except Exception as e:
            print(f"  [ERR] {hname}: {e}")

    # ── 6. Generate Globals tiddler ──
    print("\n--- Generating Globals Tiddler ---")
    try:
        title, content = generate_globals_tiddler(apidesc_globals)
        if title and content:
            path = TIDDLERS / "Globals.md"
            tid = f"# {title}\n\n{content}\n"
            path.write_text(tid, encoding="utf-8")
            print(f"  [OK] Globals -> Globals.md")
    except Exception as e:
        print(f"  [ERR] Globals: {e}")

    # ── 7. Generate article tiddlers ──
    print("\n--- Generating Article Tiddlers ---")
    articles = [
        ("Writing-a-Cuberite-plugin.html", "Writing a Cuberite Plugin"),
        ("InfoFile.html", "Using the Info.lua File"),
        ("SettingUpDecoda.html", "Setting up the Decoda Lua IDE"),
        ("SettingUpZeroBrane.html", "Setting up the ZeroBrane Studio Lua IDE"),
        ("SettingUpLuaLanguageServer.html", "Setting up Lua-Language-Server (VSCode/Emacs)"),
        ("UsingChunkStays.html", "Using ChunkStays"),
        ("WebWorldThreads.html", "Webserver vs World Threads"),
    ]
    article_count = 0
    for fname, atitle in articles:
        try:
            title, content = generate_article_tiddler(fname, atitle)
            if title and content:
                safe = re.sub(r"[^a-zA-Z0-9_-]", "_", fname.replace(".html", ""))
                path = TIDDLERS / f"{safe}.md"
                tid = f"# {title}\n\n{content}\n"
                path.write_text(tid, encoding="utf-8")
                article_count += 1
                print(f"  [OK] {fname} -> {safe}.md")
        except Exception as e:
            print(f"  [ERR] {fname}: {e}")

    # ── Summary ──
    print(f"\n{'='*50}")
    print(f"Classes:  {class_count}")
    print(f"Hooks:    {hook_count}")
    print(f"Articles: {article_count}")
    print(f"Total:    {class_count + hook_count + article_count}")
    print(f"Location: {TIDDLERS}/")
    print(f"{'='*50}")


if __name__ == "__main__":
    main()