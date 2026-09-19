# Convert HTML to markdown, then optionally to markdown AST
# markdownify not support AST, so you need convert html to markdown first

from markdownify import markdownify as md
import re


def html_to_md(html_text):
    """Convert HTML content from Desc/Returns fields to markdown."""
    if not html_text:
        return ""
    wrapped = f"<div>{html_text}</div>"
    result = md(wrapped, strip=["div"])
    lines = result.split("\n")
    cleaned = []
    for line in lines:
        line = line.rstrip()
        if line:
            cleaned.append(line)
        elif cleaned and cleaned[-1] != "":
            cleaned.append("")
    while cleaned and cleaned[-1] == "":
        cleaned.pop()
    return "\n".join(cleaned)


def type_to_md(type_str):
    """Convert a Type string to markdown, handling {{wiki links}}."""
    if not type_str:
        return ""
    m = re.match(r'\{\{(.+?)\}\}', type_str)
    if m:
        inner = m.group(1)
        if "|" in inner:
            cls, display = inner.split("|", 1)
            return f"[{display}](#{cls})"
        else:
            return f"[{inner}](#{inner})"
    return type_str