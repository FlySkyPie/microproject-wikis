This hook is called for each {{cWorld|world}} every tick (50 msec, or 20 times a second). If the
world is overloaded, the interval is larger, which is indicated by the TimeDelta parameter.

This hook is called in the world's tick thread context and thus has access to all world data
guaranteed without blocking.

## Callback function

The default name for the callback function is OnWorldTick. It has the following signature:

```lua
function MyOnWorldTick(World, TimeDelta)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| World | [cWorld](#cWorld) | World that is ticking |
| TimeDelta | number | The number of milliseconds since the previous game tick. Will not be less than 50 msec |

If the function returns false or no value, the next plugin's callback is called. If the function
returns true, no other callback is called for this event. There is no overridable behavior.
