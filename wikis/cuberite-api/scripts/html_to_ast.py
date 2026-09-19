# Convert HTML to commonmark Node AST
# HTML → markdownify → commonmark Parser → commonmark Node

from markdownify import markdownify as md
from commonmark import Parser


def html_to_commonmark(html_text: str) -> "Node":
    """Convert HTML string into a commonmark Node AST (document node)."""
    from commonmark.node import Node

    if not html_text:
        doc = Node("document", [[1, 1], [1, 1]])
        return doc
    wrapped = f"<div>{html_text}</div>"
    md_str = md(wrapped, strip=["div"])
    parser = Parser()
    return parser.parse(md_str)