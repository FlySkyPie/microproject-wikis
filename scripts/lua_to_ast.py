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


def get_table_fields(table_node):
    """Get all (key_str, value_node) pairs from a Table node, preserving order and duplicates."""
    pairs = []
    for field in table_node.fields:
        key = field.key
        if key is None:
            pairs.append((None, field.value))
        elif isinstance(key, astnodes.Name):
            pairs.append((key.id, field.value))
        elif isinstance(key, astnodes.String):
            pairs.append((decode(key.s), field.value))
        elif isinstance(key, astnodes.Number):
            pairs.append((str(int(key.n)), field.value))
        else:
            pairs.append((str(key), field.value))
    return pairs


def extract_value_nodes(table_node):
    """Extract values from a table, handling duplicate keys by converting to lists."""
    pairs = get_table_fields(table_node)
    result = {}
    for key, value in pairs:
        if key is None:
            continue
        if key in result:
            existing = result[key]
            if isinstance(existing, list):
                existing.append(value)
            else:
                result[key] = [existing, value]
        else:
            result[key] = value
    return result