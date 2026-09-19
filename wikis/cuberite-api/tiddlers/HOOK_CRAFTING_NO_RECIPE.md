This callback is called when a player places items in their {{cCraftingGrid|crafting grid}} and
Cuberite cannot find a built-in {{cCraftingRecipe|recipe}} for the combination. Plugins may provide
a recipe for the ingredients given.

## Callback function

The default name for the callback function is OnCraftingNoRecipe. It has the following signature:

```lua
function MyOnCraftingNoRecipe(Player, Grid, Recipe)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| Player | [cPlayer](#cPlayer) | The player whose crafting is reported in this hook |
| Grid | [cCraftingGrid](#cCraftingGrid) | Contents of the player's crafting grid |
| Recipe | [cCraftingRecipe](#cCraftingRecipe) | The recipe that will be used (can be filled by plugins) |

If the function returns false or no value, no recipe will be used. If the function returns true, no
other plugin will have their callback called for this event and Cuberite will use the crafting
recipe in Recipe.

FIXME: To allow plugins give suggestions and overwrite other plugins' suggestions, we should change
the behavior with returning false, so that the recipe will still be used, but fill the recipe with
empty values by default.
