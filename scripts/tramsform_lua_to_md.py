# Orchestrator: read Lua, parse, build AST, render, write

from pathlib import Path

from scripts.lua_to_ast import parse_hook, parse_class
from scripts.ast_to_ast import hook_to_commonmark, class_to_commonmark
from scripts.ast_to_md import render_commonmark

BASE = Path(__file__).parent.parent
HOOKS_DIR = BASE / ".agent-refs" / "APIDump" / "Hooks"
CLASSES_DIR = BASE / ".agent-refs" / "APIDump" / "Classes"
TIDDLERS = BASE / "tiddlers"


def write_tiddler(title: str, content: str):
    (TIDDLERS / f"{title}.md.meta").write_text(
        f"title: {title}\ntype: text/markdown\n", encoding="utf-8"
    )
    (TIDDLERS / f"{title}.md").write_text(content, encoding="utf-8")
    print(f"  [OK] {title}")


def main():
    TIDDLERS.mkdir(parents=True, exist_ok=True)

    print("Converting hooks...")
    for f in sorted(HOOKS_DIR.glob("*.lua")):
        try:
            hook = parse_hook(f.read_text(encoding="utf-8"))
            if hook:
                ast = hook_to_commonmark(hook)
                write_tiddler(hook.name, render_commonmark(ast))
        except Exception as e:
            print(f"  [ERR] Hook file {f.name}: {e}")

    print("Converting classes...")
    for f in sorted(CLASSES_DIR.glob("*.lua")):
        try:
            cls = parse_class(f.read_text(encoding="utf-8"))
            if cls:
                ast = class_to_commonmark(cls)
                write_tiddler(cls.name, render_commonmark(ast))
        except Exception as e:
            print(f"  [ERR] Class file {f.name}: {e}")


if __name__ == "__main__":
    main()