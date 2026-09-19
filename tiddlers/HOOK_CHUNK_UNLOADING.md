Cuberite calls this function when a chunk is about to be unloaded from the memory. A plugin may
force Cuberite to keep the chunk in memory by returning true.

CAUTION: Preventing the server from unloading chunks can cause the server to use too much RAM, which will adversely affect both performance and stability (i.e. your computer will get slow and crash). Return true sparingly.

## Callback function

The default name for the callback function is OnChunkUnloading. It has the following signature:

```lua
function MyOnChunkUnloading(World, ChunkX, ChunkZ)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| World | [cWorld](#cWorld) | The world from which the chunk is unloading |
| ChunkX | number | X-coord of the chunk |
| ChunkZ | number | Z-coord of the chunk |

If the function returns false or no value, the next plugin's callback is called and finally Cuberite
unloads the chunk. If the function returns true, no other callback is called for this event and the
chunk is left in the memory.
