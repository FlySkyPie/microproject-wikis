# Generate final markdown

from scripts.html_to_ast import type_to_md


def build_param_table(params):
    """Build a markdown table from Params entries."""
    if not params:
        return ""
    if isinstance(params, dict):
        params = [params]
    lines = ["| Name | Type | Notes |", "| --- | --- | --- |"]
    for p in params:
        if isinstance(p, dict):
            name = p.get("Name", "")
            ptype = p.get("Type", "")
            notes = p.get("Notes", "")
            is_optional = p.get("IsOptional", False)
            if is_optional:
                name = f"{name} (optional)"
            lines.append(f"| {name} | {type_to_md(ptype)} | {notes} |")
        elif isinstance(p, str):
            lines.append(f"| {p} | | |")
    return "\n".join(lines)


def build_returns_table(returns_r):
    """Build a markdown table from Returns entries."""
    if isinstance(returns_r, list):
        rlines = ["| Name | Type | Notes |", "| --- | --- | --- |"]
        for r in returns_r:
            if isinstance(r, dict):
                rn = r.get("Name", "")
                rt = r.get("Type", "")
                rnotes = r.get("Notes", "")
                rlines.append(f"| {rn} | {type_to_md(rt)} | {rnotes} |")
        return "\n".join(rlines)
    elif isinstance(returns_r, dict):
        rlines = ["| Name | Type | Notes |", "| --- | --- | --- |"]
        rn = returns_r.get("Name", "")
        rt = returns_r.get("Type", "")
        rnotes = returns_r.get("Notes", "")
        rlines.append(f"| {rn} | {type_to_md(rt)} | {rnotes} |")
        return "\n".join(rlines)
    elif isinstance(returns_r, str):
        return returns_r
    return ""


def clean_code_text(code_text):
    """Clean and dedent code text."""
    code_text = str(code_text)
    code_lines = code_text.strip("\n").split("\n")
    if code_lines:
        stripped = [l for l in code_lines if l.strip()]
        if stripped:
            min_indent = min(len(l) - len(l.lstrip()) for l in stripped)
            code_lines = [l[min_indent:] if len(l) >= min_indent else l for l in code_lines]
    return "\n".join(code_lines).strip()