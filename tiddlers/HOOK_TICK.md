This hook is called every game tick (50 msec, or 20 times a second). If the server is overloaded,
the interval is larger, which is indicated by the TimeDelta parameter.

This hook is called in the context of the server-tick thread, that is, the thread that takes care of
{{cClientHandle|client connections}} before they're assigned to {{cPlayer|player entities}}, and
processing console commands.

## Callback function

The default name for the callback function is OnTick. It has the following signature:

```lua
function MyOnTick(TimeDelta)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| TimeDelta | number | The number of milliseconds elapsed since the last server tick. Will not be less than 50 msec. |

If the function returns false or no value, other plugins' callbacks are called. If the function
returns true, no other callbacks are called. There is no overridable behavior.
