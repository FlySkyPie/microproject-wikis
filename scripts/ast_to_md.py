# Render commonmark Node AST into markdown string

from commonmark.node import Node


def _render_inline(parent: Node) -> str:
    """Render inline children of a node as markdown text."""
    parts = []
    child = parent.first_child
    while child is not None:
        if child.t == "text":
            parts.append(child.literal or "")
        elif child.t == "strong":
            parts.append("**")
            parts.append(_render_inline(child))
            parts.append("**")
        elif child.t == "link":
            parts.append("[")
            parts.append(_render_inline(child))
            parts.append("](" + (child.destination or "") + ")")
        elif child.t == "code":
            parts.append("`" + (child.literal or "") + "`")
        elif child.t == "softbreak":
            parts.append("\n")
        child = child.nxt
    return "".join(parts)


def render_commonmark(root: Node) -> str:
    """Walk commonmark Node AST children and produce markdown."""
    lines: list[str] = []

    child = root.first_child
    while child is not None:
        t = child.t

        if t == "heading":
            text = _render_inline(child)
            lines.append("#" * child.level + " " + text)
            lines.append("")

        elif t == "paragraph":
            text = _render_inline(child)
            lines.append(text)
            lines.append("")

        elif t == "code_block":
            lang = child.info or ""
            lines.append("```" + lang)
            lines.append((child.literal or "").rstrip())
            lines.append("```")
            lines.append("")

        elif t == "table":
            rows = []
            row = child.first_child
            while row is not None:
                cells = []
                cell = row.first_child
                while cell is not None:
                    cells.append(_render_inline(cell))
                    cell = cell.nxt
                rows.append(cells)
                row = row.nxt
            if rows:
                headers = rows[0]
                lines.append("| " + " | ".join(headers) + " |")
                lines.append("| " + " | ".join(["---"] * len(headers)) + " |")
                for body_row in rows[1:]:
                    lines.append("| " + " | ".join(body_row) + " |")
                lines.append("")

        elif t == "list":
            item = child.first_child
            while item is not None:
                para = item.first_child
                while para is not None:
                    text = _render_inline(para)
                    lines.append("- " + text)
                    lines.append("")
                    para = para.nxt
                item = item.nxt

        child = child.nxt

    while lines and lines[-1] == "":
        lines.pop()
    return "\n".join(lines) + "\n"