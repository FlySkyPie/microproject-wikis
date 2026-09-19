# Extract information from Lua files into typed Python data structures
#
# This module only does ONE thing: parse Lua → typed raw data.
# No formatting, no markdown, no HTML conversion.

from dataclasses import dataclass, field
from typing import Any

from luaparser import ast
from luaparser import astnodes

# ---- Lua AST extraction utilities ----


def decode(val):
    if isinstance(val, bytes):
        return val.decode("utf-8")
    return str(val)


def extract(node):
    """Recursively extract a Lua AST node into Python objects."""
    if isinstance(node, astnodes.Table):
        fields = node.fields
        has_named = any(
            f.key is not None and not isinstance(f.key, astnodes.Number) for f in fields
        )
        if not has_named:
            result = []
            for f in fields:
                result.append(extract(f.value))
            return result
        result = {}
        for f in fields:
            key = f.key
            if key is None:
                continue
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


# ---- Typed data structures ----

@dataclass
class ParamDef:
    name: str
    type: str
    notes: str = ""
    is_optional: bool = False


@dataclass
class ReturnDef:
    name: str = ""
    type: str = ""
    notes: str = ""


@dataclass
class OverloadData:
    notes: str = ""
    params: list[ParamDef] = field(default_factory=list)
    returns: list[ReturnDef] = field(default_factory=list)
    returns_text: str = ""
    is_static: bool = False


@dataclass
class ExampleData:
    title: str = ""
    desc: str = ""
    code: str = ""


@dataclass
class HookRaw:
    name: str
    default_fn_name: str
    called_when: str = ""
    desc_html: str = ""
    params: list[ParamDef] = field(default_factory=list)
    returns_html: str = ""
    examples: list[ExampleData] = field(default_factory=list)


@dataclass
class FunctionRaw:
    name: str
    overloads: list[OverloadData] = field(default_factory=list)


@dataclass
class ClassRaw:
    name: str
    desc_html: str = ""
    inherits: str | None = None
    functions: list[FunctionRaw] = field(default_factory=list)
    constants: dict[str, dict] = field(default_factory=dict)
    constant_groups: dict[str, dict] = field(default_factory=dict)
    variables: dict[str, dict] = field(default_factory=dict)
    additional_info: list[dict] = field(default_factory=list)


# ---- Parsing functions ----


def _dict_to_params(raw) -> list[ParamDef]:
    if isinstance(raw, dict):
        raw = [raw]
    if not isinstance(raw, list):
        return []
    result = []
    for p in raw:
        if isinstance(p, dict):
            result.append(
                ParamDef(
                    name=p.get("Name", ""),
                    type=p.get("Type", ""),
                    notes=p.get("Notes", ""),
                    is_optional=p.get("IsOptional", False),
                )
            )
        elif isinstance(p, str):
            result.append(ParamDef(name=p))
    return result


def _dict_to_returns(raw) -> tuple[list[ReturnDef], str]:
    if isinstance(raw, str):
        return [], raw
    if isinstance(raw, dict):
        raw = [raw]
    if not isinstance(raw, list):
        return [], ""
    result = []
    for r in raw:
        if isinstance(r, dict):
            result.append(
                ReturnDef(
                    name=r.get("Name", ""),
                    type=r.get("Type", ""),
                    notes=r.get("Notes", ""),
                )
            )
    return result, ""


def _dict_to_examples(raw) -> list[ExampleData]:
    if isinstance(raw, dict):
        raw = [raw]
    if not isinstance(raw, list):
        return []
    result = []
    for ex in raw:
        if isinstance(ex, dict):
            result.append(
                ExampleData(
                    title=ex.get("Title", ""),
                    desc=ex.get("Desc", ""),
                    code=ex.get("Code", ""),
                )
            )
    return result


def _get_overloads(func_value_node) -> list[dict]:
    if isinstance(func_value_node, astnodes.Table):
        fields = func_value_node.fields
        is_array = all(
            f.key is None or isinstance(f.key, astnodes.Number) for f in fields
        )
        if is_array:
            return [extract(f.value) for f in fields]
        else:
            return [extract(func_value_node)]
    return []


def _get_func_entries(fields) -> dict[str, list[dict]]:
    result = {}
    func_table_node = fields.get("Functions")
    if func_table_node is None or not isinstance(func_table_node, astnodes.Table):
        return result
    for fname_node, fval_node in get_table_fields(func_table_node):
        if fname_node is None:
            continue
        if fname_node in result:
            prev = result[fname_node]
            if isinstance(prev, list):
                prev.append(fval_node)
            else:
                result[fname_node] = [prev, fval_node]
        else:
            result[fname_node] = fval_node
    return result


def parse_hook(code: str) -> HookRaw | None:
    tree = ast.parse(code)
    ret = tree.body.body[0]
    table_node = ret.values[0]
    pairs = get_table_fields(table_node)
    for hook_name, hook_table_node in pairs:
        if hook_name is None:
            continue
        fields = extract_value_nodes(hook_table_node)
        default_fn = extract(fields.get("DefaultFnName")) if "DefaultFnName" in fields else hook_name
        return HookRaw(
            name=str(hook_name),
            default_fn_name=str(default_fn),
            called_when=str(extract(fields.get("CalledWhen")) or ""),
            desc_html=str(extract(fields.get("Desc")) or ""),
            params=_dict_to_params(extract(fields.get("Params")) if "Params" in fields else []),
            returns_html=str(extract(fields.get("Returns")) or ""),
            examples=_dict_to_examples(extract(fields.get("Examples")) if "Examples" in fields else []),
        )
    return None


def parse_class(code: str) -> ClassRaw | None:
    tree = ast.parse(code)
    ret = tree.body.body[0]
    table_node = ret.values[0]
    pairs = get_table_fields(table_node)
    for class_name, class_table_node in pairs:
        if class_name is None:
            continue
        fields = extract_value_nodes(class_table_node)
        desc_html = extract(fields.get("Desc")) or ""
        inherits = extract(fields.get("Inherits")) if "Inherits" in fields else None

        functions = []
        for func_name, func_val in sorted(_get_func_entries(fields).items()):
            overloads = []
            for raw_overload in _get_overloads(func_val):
                if not isinstance(raw_overload, dict):
                    continue
                params_r = raw_overload.get("Params")
                returns_r = raw_overload.get("Returns")
                ret_defs, ret_text = _dict_to_returns(returns_r)
                overloads.append(
                    OverloadData(
                        notes=raw_overload.get("Notes", ""),
                        params=_dict_to_params(params_r),
                        returns=ret_defs,
                        returns_text=ret_text,
                        is_static=raw_overload.get("IsStatic", False),
                    )
                )
            functions.append(FunctionRaw(name=str(func_name), overloads=overloads))

        return ClassRaw(
            name=str(class_name),
            desc_html=str(desc_html) if desc_html else "",
            inherits=str(inherits) if inherits else None,
            functions=functions,
            constants=extract(fields.get("Constants")) if "Constants" in fields else {},
            constant_groups=extract(fields.get("ConstantGroups")) if "ConstantGroups" in fields else {},
            variables=extract(fields.get("Variables")) if "Variables" in fields else {},
            additional_info=extract(fields.get("AdditionalInfo")) if "AdditionalInfo" in fields else [],
        )
    return None