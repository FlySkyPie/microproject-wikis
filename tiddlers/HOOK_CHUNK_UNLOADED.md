This hook is called when a chunk is unloaded from the memory. Though technically still in memory,
the plugin should behave as if the chunk was already not present. In particular, {{cWorld}} block
API should not be used in the area of the specified chunk.

## Callback function

The default name for the callback function is OnChunkUnloaded. It has the following signature:

```lua
function MyOnChunkUnloaded(World, ChunkX, ChunkZ)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| World | [cWorld](#cWorld) | The world from which the chunk is unloading |
| ChunkX | number | X-coord of the chunk |
| ChunkZ | number | Z-coord of the chunk |

If the function returns false or no value, the next plugin's callback is called. If the function
returns true, no other callback is called for this event. There is no behavior that plugins could
override.
