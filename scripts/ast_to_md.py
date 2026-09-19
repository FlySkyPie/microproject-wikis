# Geenrate final markdown

from pathlib import Path
from mistletoe import Document
from mistletoe.markdown_renderer import MarkdownRenderer


# You can convert AST to markdown
# with open('dev-guide.md', 'r') as fin:
#     with MarkdownRenderer(max_line_length=20) as renderer:
#         print(renderer.render(Document(fin)))