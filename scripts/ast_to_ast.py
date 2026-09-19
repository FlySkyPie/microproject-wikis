# Transform raw data or many kind of markdown AST into final form of markdown AST

from luaparser import astnodes


def extract_params(param_table_node):
    """Extract params from a Table node as a list of dicts."""
    from scripts.lua_to_ast import extract

    if param_table_node is None:
        return []
    params = extract(param_table_node) if isinstance(param_table_node, astnodes.Table) else param_table_node
    if isinstance(params, dict):
        return [params]
    if isinstance(params, list):
        return params
    return []


def get_overloads(func_value_node):
    """Get list of overload dicts for a function value node."""
    from scripts.lua_to_ast import extract

    if isinstance(func_value_node, astnodes.Table):
        fields = func_value_node.fields
        # Check if array-style (all keys are None/Number)
        is_array = all(f.key is None or isinstance(f.key, astnodes.Number) for f in fields)
        if is_array:
            # Multiple overloads
            return [extract(f.value) for f in fields]
        else:
            # Single overload (dict-style)
            return [extract(func_value_node)]
    return []