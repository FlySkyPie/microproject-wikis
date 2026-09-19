# Extract Information you need from Lua file

from luaparser import ast
from luaparser import astnodes


def lua_source_2_ast(code: str) -> astnodes.Chunk:
    return ast.parse(code)

def decode(val):
    """Decode a luaparser string value, which may be bytes."""
    if isinstance(val, bytes):
        return val.decode("utf-8")
    return str(val)

def extract(node):
    """Recursively extract a Lua AST node into Python objects."""
    if isinstance(node, astnodes.Table):
        fields = node.fields
        # Detect if pure array-style (no named keys)
        has_named = any(f.key is not None and not isinstance(f.key, astnodes.Number) for f in fields)
        if not has_named:
            # Array-style
            result = []
            for f in fields:
                result.append(extract(f.value))
            return result
        # Dict-style
        result = {}
        for f in fields:
            key = f.key
            if key is None:
                continue  # skip mixed
            if isinstance(key, astnodes.Name):
                k = key.id
            elif isinstance(key, astnodes.String):
                k = decode(key.s)
            elif isinstance(key, astnodes.Number):
                k = str(int(key.n))
            else:
                k = str(key)
            result[k] = extract(f.value)
        return result
    elif isinstance(node, astnodes.String):
        return decode(node.s)
    elif isinstance(node, astnodes.Number):
        return node.n
    elif isinstance(node, astnodes.Name):
        return node.id
    elif isinstance(node, astnodes.TrueExpr):
        return True
    elif isinstance(node, astnodes.FalseExpr):
        return False
    elif isinstance(node, astnodes.Nil):
        return None
    return None

# You can convert lua into AST
# for f in sorted(HOOKS_DIR.glob("*.lua")):
#     try:
#         code = f.read_text(encoding="utf-8")
#         tree = ast.parse(code)
#         print(ast.to_pretty_str(tree))
#     except Exception as e:
#         print(f"  [ERR] Hook file {f.name}: {e}")
