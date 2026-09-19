from pathlib import Path
from luaparser import ast
from markdownify import markdownify as md
from mistletoe import Document, HtmlRenderer
from mistletoe.markdown_renderer import MarkdownRenderer

# You can convert HTML into markdown
# md('<b>Yay</b> <a href="http://github.com">GitHub</a>')  # > '**Yay** [GitHub](http://github.com)'

# You can convert markdown into AST
# with open('foo.md', 'r') as fin:
#     doc = Document(fin)              # parse the lines into AST

# You can convert AST to markdown
# with open('dev-guide.md', 'r') as fin:
#     with MarkdownRenderer(max_line_length=20) as renderer:
#         print(renderer.render(mistletoe.Document(fin)))

BASE = Path(__file__).parent
ROOT = BASE.parent
APIDUMP = ROOT / ".agent-refs" / "APIDump"
TIDDLERS = ROOT / "tiddlers"
CLASSES_DIR = APIDUMP / "Classes"
HOOKS_DIR = APIDUMP / "Hooks"


for f in sorted(CLASSES_DIR.glob("*.lua")):
    try:
        code = f.read_text(encoding="utf-8")
        tree = ast.parse(code)
        # TODO convert the lua into markdown document
        print(ast.to_pretty_str(tree))
    except Exception as e:
        print(f"  [ERR] Class file {f.name}: {e}")

for f in sorted(HOOKS_DIR.glob("*.lua")):
    try:
        code = f.read_text(encoding="utf-8")
        tree = ast.parse(code)
        # TODO convert the lua into markdown document
        print(ast.to_pretty_str(tree))
    except Exception as e:
        print(f"  [ERR] Hook file {f.name}: {e}")