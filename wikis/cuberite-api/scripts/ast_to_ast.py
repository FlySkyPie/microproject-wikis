# Transform raw typed data into commonmark Node AST

from commonmark.node import Node

from scripts.html_to_ast import html_to_commonmark
from scripts.lua_to_ast import HookRaw, ClassRaw, ParamDef, ReturnDef, OverloadData


# ---- Helpers ----


def _make_text(literal: str) -> Node:
    n = Node("text", [[1, 1], [1, 1]])
    n.literal = literal
    return n


def _make_strong(text: str) -> Node:
    n = Node("strong", [[1, 1], [1, 1]])
    n.append_child(_make_text(text))
    return n


def _make_link(text: str, target: str) -> Node:
    n = Node("link", [[1, 1], [1, 1]])
    n.destination = target
    n.append_child(_make_text(text))
    return n


def _make_paragraph(spans: list[Node]) -> Node:
    n = Node("paragraph", [[1, 1], [1, 1]])
    for s in spans:
        n.append_child(s)
    return n


def _make_heading(level: int, text: str) -> Node:
    n = Node("heading", [[1, 1], [1, 1]])
    n.level = level
    n.append_child(_make_text(text))
    return n


def _make_cell(text: str) -> Node:
    cell = Node("td", [[1, 1], [1, 1]])
    cell.append_child(_make_text(text))
    return cell


def _make_cell_with_link(type_str: str) -> Node:
    cell = Node("td", [[1, 1], [1, 1]])
    cell.append_child(_type_link(type_str))
    return cell


def _clean_code(code: str) -> str:
    lines = code.strip("\n").split("\n")
    stripped = [l for l in lines if l.strip()]
    if stripped:
        min_indent = min(len(l) - len(l.lstrip()) for l in stripped)
        lines = [l[min_indent:] if len(l) >= min_indent else l for l in lines]
    return "\n".join(lines).strip()


def _make_code_fence(lang: str, code: str) -> Node:
    n = Node("code_block", [[1, 1], [1, 1]])
    n.info = lang
    n.literal = _clean_code(code) + "\n"
    n.is_fenced = True
    n.fence_length = 3
    n.fence_char = "`"
    return n


def _type_link(type_str: str) -> Node:
    if not type_str:
        return _make_text("")
    import re
    m = re.match(r'\{\{(.+?)\}\}', type_str)
    if m:
        inner = m.group(1)
        if "|" in inner:
            cls, display = inner.split("|", 1)
            return _make_link(display, "#" + cls)
        else:
            return _make_link(inner, "#" + inner)
    return _make_text(type_str)


def _transplant(source: Node, target: Node):
    """Move all children from source node to target."""
    child = source.first_child
    while child is not None:
        nxt = child.nxt
        child.unlink()
        target.append_child(child)
        child = nxt


def _build_param_table(params: list[ParamDef]) -> Node:
    table = Node("table", [[1, 1], [1, 1]])
    header = Node("tr", [[1, 1], [1, 1]])
    header.append_child(_make_cell("Name"))
    header.append_child(_make_cell("Type"))
    header.append_child(_make_cell("Notes"))
    table.append_child(header)
    for p in params:
        row = Node("tr", [[1, 1], [1, 1]])
        name = p.name + " (optional)" if p.is_optional else p.name
        cell_name = Node("td", [[1, 1], [1, 1]])
        cell_name.append_child(_make_text(name))
        row.append_child(cell_name)
        cell_type = Node("td", [[1, 1], [1, 1]])
        cell_type.append_child(_type_link(p.type))
        row.append_child(cell_type)
        row.append_child(_make_cell(p.notes))
        table.append_child(row)
    return table


def _build_returns_table(returns: list[ReturnDef]) -> Node:
    table = Node("table", [[1, 1], [1, 1]])
    header = Node("tr", [[1, 1], [1, 1]])
    header.append_child(_make_cell("Name"))
    header.append_child(_make_cell("Type"))
    header.append_child(_make_cell("Notes"))
    table.append_child(header)
    for r in returns:
        row = Node("tr", [[1, 1], [1, 1]])
        row.append_child(_make_cell(r.name))
        cell_type = Node("td", [[1, 1], [1, 1]])
        cell_type.append_child(_type_link(r.type))
        row.append_child(cell_type)
        row.append_child(_make_cell(r.notes))
        table.append_child(row)
    return table


# ---- Hook layout ----

def hook_to_commonmark(hook: HookRaw) -> Node:
    doc = Node("document", [[1, 1], [1, 1]])

    # Description
    if hook.desc_html:
        desc_ast = html_to_commonmark(hook.desc_html)
        _transplant(desc_ast, doc)

    # ## Callback function
    doc.append_child(_make_heading(2, "Callback function"))
    doc.append_child(_make_paragraph([
        _make_text(
            f"The default name for the callback function is {hook.default_fn_name}. "
            f"It has the following signature:"
        ),
    ]))

    param_names = ", ".join(p.name for p in hook.params)
    doc.append_child(_make_code_fence("lua", f"function My{hook.default_fn_name}({param_names})"))

    # ## Parameters
    if hook.params:
        doc.append_child(_make_heading(2, "Parameters"))
        doc.append_child(_build_param_table(hook.params))

    # Returns
    if hook.returns_html:
        ret_ast = html_to_commonmark(hook.returns_html)
        _transplant(ret_ast, doc)

    # ## Code examples
    if hook.examples:
        doc.append_child(_make_heading(2, "Code examples"))
        for ex in hook.examples:
            if ex.title:
                doc.append_child(_make_heading(3, ex.title))
            if ex.desc:
                doc.append_child(_make_paragraph([_make_text(str(ex.desc))]))
            if ex.code:
                doc.append_child(_make_code_fence("lua", ex.code))

    return doc


# ---- Class layout ----

def class_to_commonmark(cls: ClassRaw) -> Node:
    doc = Node("document", [[1, 1], [1, 1]])

    # Inherits
    if cls.inherits:
        doc.append_child(_make_paragraph([
            _make_strong("Inherits from: "),
            _make_link(cls.inherits, "#" + cls.inherits),
        ]))

    # Description
    if cls.desc_html:
        desc_ast = html_to_commonmark(cls.desc_html)
        _transplant(desc_ast, doc)

    # ## Functions
    if cls.functions:
        doc.append_child(_make_heading(2, "Functions"))
        for func in cls.functions:
            for i, ol in enumerate(func.overloads):
                sig = f"{func.name}({', '.join(p.name for p in ol.params)})"
                if ol.is_static:
                    sig = f"**Static** {sig}"
                label = f"Overload {i + 1}: {sig}" if len(func.overloads) > 1 else sig
                doc.append_child(_make_heading(3, label))

                if ol.params:
                    doc.append_child(_build_param_table(ol.params))
                if ol.returns:
                    doc.append_child(_make_paragraph([_make_strong("Returns:")]))
                    doc.append_child(_build_returns_table(ol.returns))
                if ol.returns_text:
                    doc.append_child(_make_paragraph([
                        _make_strong("Returns:"),
                        _make_text(" " + ol.returns_text),
                    ]))
                if ol.notes:
                    doc.append_child(_make_paragraph([_make_text(str(ol.notes))]))

    # ## Constants
    if cls.constants:
        doc.append_child(_make_heading(2, "Constants"))
        table = Node("table", [[1, 1], [1, 1]])
        header = Node("tr", [[1, 1], [1, 1]])
        header.append_child(_make_cell("Name"))
        header.append_child(_make_cell("Notes"))
        table.append_child(header)
        for cname in sorted(cls.constants.keys()):
            cinfo = cls.constants[cname]
            notes = cinfo.get("Notes", "") if isinstance(cinfo, dict) else ""
            row = Node("tr", [[1, 1], [1, 1]])
            row.append_child(_make_cell(cname))
            row.append_child(_make_cell(notes))
            table.append_child(row)
        doc.append_child(table)

    # ## Constant Groups
    if cls.constant_groups:
        doc.append_child(_make_heading(2, "Constant Groups"))
        for gname in sorted(cls.constant_groups.keys()):
            ginfo = cls.constant_groups[gname]
            if isinstance(ginfo, dict):
                tb = ginfo.get("TextBefore", "")
                inc = ginfo.get("Include", [])
                ta = ginfo.get("TextAfter", "")
                if tb:
                    doc.append_child(_make_paragraph([_make_text(str(tb))]))
                doc.append_child(_make_heading(3, gname))
                if isinstance(inc, list):
                    doc.append_child(_make_paragraph([_make_text(" | ".join(inc))]))
                if ta:
                    doc.append_child(_make_paragraph([_make_text(str(ta))]))

    # ## Variables
    if cls.variables:
        doc.append_child(_make_heading(2, "Variables"))
        table = Node("table", [[1, 1], [1, 1]])
        header = Node("tr", [[1, 1], [1, 1]])
        header.append_child(_make_cell("Name"))
        header.append_child(_make_cell("Type"))
        header.append_child(_make_cell("Notes"))
        table.append_child(header)
        for vname in sorted(cls.variables.keys()):
            vinfo = cls.variables[vname]
            if isinstance(vinfo, dict):
                row = Node("tr", [[1, 1], [1, 1]])
                row.append_child(_make_cell(vname))
                row.append_child(_make_cell_with_link(vinfo.get("Type", "")))
                row.append_child(_make_cell(vinfo.get("Notes", "")))
                table.append_child(row)
        doc.append_child(table)

    # ## Additional Info
    if cls.additional_info:
        doc.append_child(_make_heading(2, "Additional Info"))
        infos = cls.additional_info
        if isinstance(infos, dict):
            infos = [infos]
        if isinstance(infos, list):
            for info in infos:
                if isinstance(info, dict):
                    header = info.get("Header", "")
                    contents = info.get("Contents", "")
                    if header:
                        doc.append_child(_make_heading(3, str(header)))
                    if contents:
                        cont_ast = html_to_commonmark(str(contents))
                        _transplant(cont_ast, doc)

    return doc