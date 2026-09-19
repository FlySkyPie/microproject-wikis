This hook is called whenever a {{cWorld|world}} is initialized.

## Callback function

The default name for the callback function is OnWorldStarted. It has the following signature:

```lua
function MyOnWorldStarted(World)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| World | [cWorld](#cWorld) | World that is started |

If the function returns false or no value, the next plugin's callback is called. If the function
returns true, no other callback is called for this event. There is no overridable behavior.
