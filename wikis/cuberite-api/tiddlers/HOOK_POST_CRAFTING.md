This hook is called when a {{cPlayer|player}} changes contents of their
{{cCraftingGrid|crafting grid}}, after the recipe has been established by Cuberite. Plugins may use
this to modify the resulting recipe or provide an alternate recipe.

If a plugin implements custom recipes, it should do so using the {{OnPreCrafting|HOOK_PRE_CRAFTING}}
hook, because that will save the server from going through the built-in recipes. The
HOOK_POST_CRAFTING hook is intended as a notification, with a chance to tweak the result.

Note that this hook is not called if a built-in recipe is not found;
{{OnCraftingNoRecipe|HOOK_CRAFTING_NO_RECIPE}} is called instead in such a case.

## Callback function

The default name for the callback function is OnPostCrafting. It has the following signature:

```lua
function MyOnPostCrafting(Player, Grid, Recipe)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| Player | [cPlayer](#cPlayer) | The player who has changed their crafting grid contents |
| Grid | [cCraftingGrid](#cCraftingGrid) | The new crafting grid contents |
| Recipe | [cCraftingRecipe](#cCraftingRecipe) | The recipe that Cuberite has decided to use (can be tweaked by plugins) |

If the function returns false or no value, other plugins' callbacks are called. If the function
returns true, no other callbacks are called for this event. In either case, Cuberite uses the value
of Recipe as the recipe to be presented to the player.
