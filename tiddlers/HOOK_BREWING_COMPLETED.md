This hook is called whenever a {{cBrewingstandEntity|brewing stand}} has completed the brewing process.
See also the {{OnBrewingCompleting|HOOK_BREWING_COMPLETING}} hook for a similar hook, is called when a
brewing process is completing.

## Callback function

The default name for the callback function is OnBrewingCompleted. It has the following signature:

```lua
function MyOnBrewingCompleted(World, Brewingstand)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| World | [cWorld](#cWorld) | World where the brewing stand resides. |
| Brewingstand | [cBrewingstandEntity](#cBrewingstandEntity) | The brewing stand that completed the brewing process. |

If the function returns false or no value, Cuberite calls other plugins with this event. If the
function returns true, no other plugin is called for this event.
