# markdownify not support AST, so you need convert html to markdown first, then convert into AST

from markdownify import markdownify as md
from pathlib import Path
from mistletoe import Document

# You can convert HTML into markdown
# md('<b>Yay</b> <a href="http://github.com">GitHub</a>')  # > '**Yay** [GitHub](http://github.com)'

# You can convert markdown into AST
# with open('foo.md', 'r') as fin:
#     doc = Document(fin)              # parse the lines into AST
