This hook is called after a chunk is either generated or loaded from the disk. The chunk is
already available for manipulation using the {{cWorld}} API. This is a notification-only callback,
there is no behavior that plugins could override.

## Callback function

The default name for the callback function is OnChunkAvailable. It has the following signature:

```lua
function MyOnChunkAvailable(World, ChunkX, ChunkZ)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| World | [cWorld](#cWorld) | The world to which the chunk belongs |
| ChunkX | number | X-coord of the chunk |
| ChunkZ | number | Z-coord of the chunk |

If the function returns false or no value, the next plugin's callback is called. If the function
returns true, no other callback is called for this event.
