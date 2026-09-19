# Orchestrator: Lua → AST → transformed AST → markdown
#
# This script uses the AST pipeline modules:
#   lua_to_ast.py   - Parse Lua files into Python objects
#   html_to_ast.py  - Convert HTML descriptions to markdown
#   ast_to_ast.py   - Transform raw data dictionaries
#   ast_to_md.py    - Generate final markdown strings

from pathlib import Path

from luaparser import ast, astnodes

from scripts.lua_to_ast import lua_source_2_ast, extract, get_table_fields, extract_value_nodes
from scripts.html_to_ast import html_to_md, type_to_md
from scripts.ast_to_ast import extract_params, get_overloads
from scripts.ast_to_md import build_param_table, build_returns_table, clean_code_text


BASE = Path(__file__).parent
ROOT = BASE.parent
APIDUMP = ROOT / ".agent-refs" / "APIDump"
TIDDLERS = ROOT / "tiddlers"
CLASSES_DIR = APIDUMP / "Classes"
HOOKS_DIR = APIDUMP / "Hooks"


def convert_hook(fname, code, tree):
    """Convert a hook Lua file to markdown tiddler."""
    ret = tree.body.body[0]
    table_node = ret.values[0]
    pairs = get_table_fields(table_node)

    for hook_name, hook_table_node in pairs:
        if hook_name is None:
            continue
        fields = extract_value_nodes(hook_table_node)

        title = hook_name
        default_fn = extract(fields.get("DefaultFnName")) if "DefaultFnName" in fields else title
        desc_html = extract(fields.get("Desc")) or ""
        params_val = extract(fields.get("Params")) if "Params" in fields else []
        returns_val = extract(fields.get("Returns")) or ""
        examples_val = extract(fields.get("Examples")) if "Examples" in fields else []

        # Desc HTML to markdown
        desc_md = html_to_md(str(desc_html)) if desc_html else ""

        parts = []
        if desc_md:
            parts.append(desc_md)
            parts.append("")

        # Callback function section
        parts.append("## Callback function")
        parts.append("")
        parts.append(f"The default name for the callback function is {default_fn}. It has the following signature:")
        parts.append("")

        param_names = []
        if isinstance(params_val, dict):
            param_names.append(params_val.get("Name", "..."))
        elif isinstance(params_val, list):
            for p in params_val:
                if isinstance(p, dict):
                    param_names.append(p.get("Name", "..."))

        parts.append("```lua")
        parts.append(f"function My{default_fn}({', '.join(param_names)})")
        parts.append("```")
        parts.append("")

        # Parameters section
        if params_val:
            parts.append("## Parameters")
            parts.append("")
            parts.append(build_param_table(params_val))
            parts.append("")

        # Returns section
        if returns_val:
            returns_md = html_to_md(str(returns_val))
            parts.append(returns_md)
            parts.append("")

        # Code examples
        if examples_val:
            if isinstance(examples_val, dict):
                examples_val = [examples_val]
            if isinstance(examples_val, list):
                parts.append("## Code examples")
                parts.append("")
                for i, ex in enumerate(examples_val):
                    if isinstance(ex, dict):
                        ex_title = ex.get("Title", f"Example {i + 1}")
                        ex_desc = ex.get("Desc", "")
                        ex_code = ex.get("Code", "")
                        parts.append(f"### {ex_title}")
                        parts.append("")
                        if ex_desc:
                            parts.append(str(ex_desc))
                            parts.append("")
                        if ex_code:
                            clean_code = clean_code_text(ex_code)
                            parts.append("```lua")
                            parts.append(clean_code)
                            parts.append("```")
                            parts.append("")

        content = "\n".join(parts).strip() + "\n"

        meta_path = TIDDLERS / f"{title}.md.meta"
        md_path = TIDDLERS / f"{title}.md"
        meta_path.write_text(f"title: {title}\ntype: text/markdown\n", encoding="utf-8")
        md_path.write_text(content, encoding="utf-8")
        print(f"  [OK] Hook {title}")


def convert_class(fname, code, tree):
    """Convert a class Lua file to markdown tiddler(s)."""
    ret = tree.body.body[0]
    table_node = ret.values[0]
    pairs = get_table_fields(table_node)

    for class_name, class_table_node in pairs:
        if class_name is None:
            continue
        fields = extract_value_nodes(class_table_node)

        title = class_name
        desc_html = extract(fields.get("Desc")) or ""
        inherits = extract(fields.get("Inherits")) if "Inherits" in fields else None

        # Functions - handle duplicates via extract_value_nodes
        func_entries = {}
        if "Functions" in fields:
            func_table_node = fields["Functions"]
            if isinstance(func_table_node, astnodes.Table):
                for fname_node, fval_node in get_table_fields(func_table_node):
                    if fname_node is None:
                        continue
                    if fname_node in func_entries:
                        prev = func_entries[fname_node]
                        if isinstance(prev, list):
                            prev.append(fval_node)
                        else:
                            func_entries[fname_node] = [prev, fval_node]
                    else:
                        func_entries[fname_node] = fval_node

        # Constants
        constants = extract(fields.get("Constants")) if "Constants" in fields else {}

        # ConstantGroups
        constant_groups = extract(fields.get("ConstantGroups")) if "ConstantGroups" in fields else {}

        # Variables
        variables = extract(fields.get("Variables")) if "Variables" in fields else {}

        # AdditionalInfo
        additional_info = extract(fields.get("AdditionalInfo")) if "AdditionalInfo" in fields else []

        desc_md = html_to_md(str(desc_html)) if desc_html else ""

        parts = []
        if inherits:
            parts.append(f"**Inherits from:** [{inherits}](#{inherits})")
            parts.append("")
        if desc_md:
            parts.append(desc_md)
            parts.append("")

        # Functions
        if func_entries:
            parts.append("## Functions")
            parts.append("")
            for func_name in sorted(func_entries.keys()):
                func_val = func_entries[func_name]
                overloads = get_overloads(func_val)

                for i, overload in enumerate(overloads):
                    if not isinstance(overload, dict):
                        continue
                    notes = overload.get("Notes", "")
                    params_r = overload.get("Params")
                    returns_r = overload.get("Returns")
                    is_static = overload.get("IsStatic", False)

                    param_names = []
                    if isinstance(params_r, dict):
                        param_names.append(params_r.get("Name", "?"))
                    elif isinstance(params_r, list):
                        for p in params_r:
                            if isinstance(p, dict):
                                name = p.get("Name", "?")
                                if p.get("IsOptional", False):
                                    name = f"[{name}]"
                                param_names.append(name)

                    sig = f"{func_name}({', '.join(param_names)})"
                    if is_static:
                        sig = f"**Static** {sig}"

                    if len(overloads) > 1:
                        parts.append(f"### Overload {i + 1}: {sig}")
                    else:
                        parts.append(f"### {sig}")
                    parts.append("")

                    if params_r:
                        tbl = build_param_table(params_r)
                        if tbl:
                            parts.append(tbl)
                            parts.append("")
                    if returns_r:
                        parts.append("**Returns:**")
                        parts.append("")
                        rtbl = build_returns_table(returns_r)
                        if rtbl:
                            parts.append(rtbl)
                        parts.append("")
                    if notes:
                        parts.append(str(notes))
                        parts.append("")

        # Constants
        if constants and isinstance(constants, dict):
            parts.append("## Constants")
            parts.append("")
            clines = ["| Name | Notes |", "| --- | --- |"]
            for cname in sorted(constants.keys()):
                cinfo = constants[cname]
                cnotes = cinfo.get("Notes", "") if isinstance(cinfo, dict) else ""
                clines.append(f"| {cname} | {cnotes} |")
            parts.append("\n".join(clines))
            parts.append("")

        # ConstantGroups
        if constant_groups and isinstance(constant_groups, dict):
            parts.append("## Constant Groups")
            parts.append("")
            for gname in sorted(constant_groups.keys()):
                ginfo = constant_groups[gname]
                if isinstance(ginfo, dict):
                    include = ginfo.get("Include", [])
                    text_before = ginfo.get("TextBefore", "")
                    text_after = ginfo.get("TextAfter", "")
                    if text_before:
                        parts.append(str(text_before))
                        parts.append("")
                    parts.append(f"### {gname}")
                    parts.append("")
                    if isinstance(include, list):
                        parts.append(" | ".join(include))
                        parts.append("")
                    if text_after:
                        parts.append(str(text_after))
                        parts.append("")

        # Variables
        if variables and isinstance(variables, dict):
            parts.append("## Variables")
            parts.append("")
            vlines = ["| Name | Type | Notes |", "| --- | --- | --- |"]
            for vname in sorted(variables.keys()):
                vinfo = variables[vname]
                if isinstance(vinfo, dict):
                    vtype = vinfo.get("Type", "")
                    vnotes = vinfo.get("Notes", "")
                    vlines.append(f"| {vname} | {type_to_md(vtype)} | {vnotes} |")
            parts.append("\n".join(vlines))
            parts.append("")

        # AdditionalInfo
        if additional_info:
            if isinstance(additional_info, dict):
                additional_info = [additional_info]
            parts.append("## Additional Info")
            parts.append("")
            if isinstance(additional_info, list):
                for info in additional_info:
                    if isinstance(info, dict):
                        header = info.get("Header", "")
                        contents = info.get("Contents", "")
                        if header:
                            parts.append(f"### {header}")
                            parts.append("")
                        if contents:
                            cm = html_to_md(str(contents))
                            parts.append(cm)
                            parts.append("")

        content = "\n".join(parts).strip() + "\n"

        meta_path = TIDDLERS / f"{title}.md.meta"
        md_path = TIDDLERS / f"{title}.md"
        meta_path.write_text(f"title: {title}\ntype: text/markdown\n", encoding="utf-8")
        md_path.write_text(content, encoding="utf-8")
        print(f"  [OK] Class {title}")


def main():
    TIDDLERS.mkdir(parents=True, exist_ok=True)

    print("Converting hooks...")
    for f in sorted(HOOKS_DIR.glob("*.lua")):
        try:
            code = f.read_text(encoding="utf-8")
            tree = ast.parse(code)
            convert_hook(f.name, code, tree)
        except Exception as e:
            print(f"  [ERR] Hook file {f.name}: {e}")

    print("Converting classes...")
    for f in sorted(CLASSES_DIR.glob("*.lua")):
        try:
            code = f.read_text(encoding="utf-8")
            tree = ast.parse(code)
            convert_class(f.name, code, tree)
        except Exception as e:
            print(f"  [ERR] Class file {f.name}: {e}")


if __name__ == "__main__":
    main()