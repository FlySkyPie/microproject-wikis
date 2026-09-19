# AGENTS.md — Cuberite API Docs Wiki

## Project Overview

This is a **TiddlyWiki5** wiki that serves as the **Cuberite API Documentation** site. It documents the Lua plugin API for the [Cuberite](https://cuberite.org) Minecraft server. The live site is at `https://api.cuberite.org/`.

The actual API documentation content (class definitions, hooks, articles) lives inside `.agent-refs/APIDump/` — that is the **source of truth** for what goes on the wiki. The `.agent-refs` directory is a reference copy of Cuberite's built-in APIDump plugin.

## Essential Commands

| Command | What it does |
|---|---|
| `pnpm start` | Starts TiddlyWiki dev server (`tiddlywiki . --listen`) |
| `pnpm run build` | Full build (bundle + static) |
| `pnpm run build:bundle` | Generates offline `index.html` from TiddlyWiki |
| `pnpm run build:static` | Copies `public/*` to `output/` |

The wiki runs on **TiddlyWiki5 v5.3.3** via the `tiddlywiki` npm package.

## Code Organization

```
.agent-refs/APIDump/       ← THE source of truth for API docs (snapshot of Cuberite's plugin)
├── APIDesc.lua            ← Master API description file — defines ALL classes/functions/hooks/globals
├── main_APIDump.lua       ← Plugin entrypoint; reads APIDesc & generates HTML output
├── _preload.lua           ← Plugin sandboxing (replaces _G with empty env + __index)
├── lualanguageserver.lua  ← Generates Lua Language Server type definitions from API descriptions
├── Classes/               ← Individual class documentation files (cWorld.lua, cBlockArea.lua, etc.)
├── Hooks/                 ← Individual hook documentation files (OnTick.lua, OnPlayerJoined.lua, etc.)
├── Static/                ← Static assets (images for setup guides, .gitignore)
├── *.html                 ← Informational articles (Writing-a-Cuberite-plugin, InfoFile, setup guides)
├── *.js / *.css           ← Client-side syntax highlighting / styling for generated HTML docs

tiddlers/                  ← TiddlyWiki content files (.tid format)
  ├── $__SiteTitle.tid     ← Wiki title
  ├── $__SiteSubtitle.tid  ← Wiki subtitle
  ├── $__StoryList.tid     ← Default story list
  └── ...

plugins/                   ← TiddlyWiki plugins
  ├── katex/               ← LaTeX rendering
  ├── markdown/            ← Markdown parsing
  ├── relink/              ← Link management
  ├── relink-fieldnames/
  ├── relink-markdown/
  └── relink-titles/

tiddlywiki.info            ← TiddlyWiki config (plugins, themes, build steps)
tsconfig.json              ← TypeScript config (points to "cli" dir that doesn't exist yet)
public/                    ← Static files (favicon.ico)
```

## APIDump Plugin Architecture

The APIDump plugin runs **inside the Cuberite server**. It:

1. **Scans the global environment** at runtime (`main_APIDump.lua:CreateAPITables()`) to discover all Cuberite API classes, functions, constants, and globals exposed to Lua.
2. **Loads descriptons** from `APIDesc.lua` and individual `Classes/*.lua` / `Hooks/*.lua` files — these contain prose descriptions, parameter types, return types, notes.
3. **Merges** the runtime-discovered API with the authored descriptions.
4. **Generates HTML** class pages, hook pages, and an index page into `API/` directory.
5. **Generates Lua Language Server** type definitions into `LLS/cuberite/library/`.

The `.agent-refs/APIDump/` directory is a frozen copy of this plugin — it's the **reference documentation content**.

## API Documentation Format

Every class and hook is a Lua file returning a table with this structure:

### Class format (`Classes/cWorld.lua`)
```lua
return {
  cClassName = {
    Desc = "Description text with {{CrossClassLinks}}",
    Functions = {
      FunctionName = {
        {
          Params = {
            { Name = "param1", Type = "number" },
            { Name = "param2", Type = "cClass#eEnum", IsOptional = true },
          },
          Returns = {
            { Type = "boolean" },
          },
          Notes = "Description of this overload",
        },
        -- Second overload:
        {
          Params = { ... },
          Returns = { ... },
          Notes = "Alternative signature",
        },
      },
    },
    Constants = {
      ConstantName = { Notes = "..." },
    },
    ConstantGroups = {
      eEnum = {
        Include = {"const1", "const2"},
        TextBefore = "...",
        TextAfter = "...",
        ShowInDescendants = false,
      },
    },
    Variables = {
      VariableName = { Type = "string", Notes = "..." },
    },
    AdditionalInfo = {
      { Header = "Title", Contents = "Detailed info" },
    },
    Inherits = "ParentClassName",  -- if applicable
  },
}
```

### Hook format (`Hooks/OnTick.lua`)
```lua
return {
  HOOK_TICK = {
    CalledWhen = "Every server tick (approximately 20 times per second)",
    DefaultFnName = "OnTick",  -- also used as pagename
    Desc = [[Description...]],
    Params = {
      { Name = "TimeDelta", Type = "number", Notes = "..." },
    },
    Returns = [[If the function returns false or no value...]],
  },
}
```

## Naming Conventions

- **Classes**: PascalCase with `c` prefix (e.g., `cWorld`, `cBlockArea`, `cPlugin`)
- **Hooks**: `HOOK_UPPER_SNAKE_CASE` constant names; `OnPascalCase` default function names
- **Functions**: PascalCase (e.g., `BroadcastBlockAction`, `GetFolderName`)
- **Constants**: Mixed case, often grouped into enums via `ConstantGroups`
- **Type references**: `ClassName#EnumName` syntax for enum/constant types (e.g., `cPluginManager#ePluginStatus`)
- **Source filenames**: Match the class/hook identifier name

## Gotchas & Non-Obvious Patterns

1. **Duplicate class docs are detected**: `main_APIDump.lua` warns and logs to `DuplicateDocs.txt` when a class is documented in multiple files.
2. **Link syntax**: Docs use `{{ClassName}}` and `{{ClassName|DisplayText}}` syntax which gets linkified to `.html` pages. External URLs (`http://`, `https://`) pass through unmodified.
3. **Functions can have multiple overloads**: Each function is an **array** of overload tables, not a single table. A function with one overload still wraps it in `{ ... }`.
4. **`_preload.lua` replaces _G**: The plugin sandboxes itself by replacing the global environment — any global created by the plugin won't be counted as part of the API.
5. **`IsStatic = true`** on a function means it's a static/class method, not an instance method.
6. **`constructor`** as a function name maps to `__call` in LLS output (and `__meta` for `operator`).
7. **Optional params** use `IsOptional = true`; the LLS export appends `?` to the parameter name.
8. **`Type = "self"`** in Returns means the function returns the object it was called on.
9. **Relative vs absolute coords**: Classes like `cBlockArea` have paired functions (e.g., `SetBlock` vs `SetBlockRel`) — one for world coords, one for area-local coords.
10. **Thread safety**: Docs routinely mention which thread a function/hook runs on (tick thread, server thread, etc.). Functions that return objects via callbacks do so because of thread safety guarantees.

## Wiki Content (Tiddlers)

Tiddlers are the individual wiki pages stored in `tiddlers/` as `.tid` files with a specific metadata format (title, tags, type, etc.). These are what gets rendered through the TiddlyWiki engine. The `.agent-refs/APIDump/` documentation files are separate — they are consumed by the APIDump plugin, not directly by TiddlyWiki.

## No TypeScript Source Yet

The `tsconfig.json` points to a `cli/` directory that doesn't exist. There are no `.ts` source files in the repo. If TypeScript code is added, it should go under `cli/` and follow strict mode (noUnusedLocals, noUnusedParameters, noFallthroughCasesInSwitch).