This hook is called after the weather has changed in a {{cWorld|world}}. The new weather has already
been sent to the clients.

See also the {{OnWeatherChanging|HOOK_WEATHER_CHANGING}} hook for a similar hook called before the
change.

## Callback function

The default name for the callback function is OnWeatherChanged. It has the following signature:

```lua
function MyOnWeatherChanged(World)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| World | [cWorld](#cWorld) | World for which the weather has changed |

If the function returns false or no value, the next plugin's callback is called. If the function
returns true, no other callback is called for this event. There is no overridable behavior.
