This hook is called when the {{cPlayer|player}} right-clicks an {{cEntity|entity}}. Plugins may
override the default behavior or even cancel the default processing.

## Callback function

The default name for the callback function is OnPlayerRightClickingEntity. It has the following signature:

```lua
function MyOnPlayerRightClickingEntity(Player, Entity)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| Player | [cPlayer](#cPlayer) | The player who has right-clicked the entity |
| Entity | [cEntity](#cEntity) | The entity that has been right-clicked |

If the functino returns false or no value, Cuberite calls other plugins' callbacks and finally does
the default processing for the right-click. If the function returns true, no other callbacks are
called and the default processing is skipped.
