This hook is called when a {{cPlayer|player}} changes contents of their
{{cCraftingGrid|crafting grid}}, before the built-in recipes are searched for a match by Cuberite.
Plugins may use this hook to provide a custom recipe.

If you intend to tweak built-in recipes, use the {{OnPostCrafting|HOOK_POST_CRAFTING}} hook, because
that will be called once the built-in recipe is matched.

Also note a third hook, {{OnCraftingNoRecipe|HOOK_CRAFTING_NO_RECIPE}}, that is called when Cuberite
cannot find any built-in recipe for the given ingredients.

## Callback function

The default name for the callback function is OnPreCrafting. It has the following signature:

```lua
function MyOnPreCrafting(Player, Grid, Recipe)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| Player | [cPlayer](#cPlayer) | The player who has changed their crafting grid contents |
| Grid | [cCraftingGrid](#cCraftingGrid) | The new crafting grid contents |
| Recipe | [cCraftingRecipe](#cCraftingRecipe) | The recipe that Cuberite will use. Modify this object to change the recipe |

If the function returns false or no value, other plugins' callbacks are called and then Cuberite
searches the built-in recipes. The Recipe output parameter is ignored in this case.

If the function returns true, no other callbacks are called for this event and Cuberite uses the
recipe stored in the Recipe output parameter.
