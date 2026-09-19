This hook is called whenever a {{cBrewingstandEntity|brewing stand}} is completing the brewing process. Plugins may
refuse the completing of the brewing process.

See also the {{OnBrewingCompleted|HOOK_BREWING_COMPLETED}} hook for a similar hook, is called after the
brewing process has been completed.

## Callback function

The default name for the callback function is OnBrewingCompleting. It has the following signature:

```lua
function MyOnBrewingCompleting(World, Brewingstand)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| World | [cWorld](#cWorld) | World where the brewing stand resides. |
| Brewingstand | [cBrewingstandEntity](#cBrewingstandEntity) | The brewing stand that completes the brewing process. |

If the function returns false or no value, Cuberite calls other plugins with this event. If the function returns true,
no other plugin's callback is called and the brewing process is canceled.
