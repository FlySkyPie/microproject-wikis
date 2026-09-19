This hook is called when world generator finished its work on a chunk. The chunk data has already
been generated and is about to be stored in the {{cWorld|world}}. A plugin may provide some
last-minute finishing touches to the generated data. Note that the chunk is not yet stored in the
world, so regular {{cWorld}} block API will not work! Instead, use the {{cChunkDesc}} object
received as the parameter.

See also the {{OnChunkGenerating|HOOK_CHUNK_GENERATING}} hook.

## Callback function

The default name for the callback function is OnChunkGenerated. It has the following signature:

```lua
function MyOnChunkGenerated(World, ChunkX, ChunkZ, ChunkDesc)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| World | [cWorld](#cWorld) | The world to which the chunk will be added |
| ChunkX | number | X-coord of the chunk |
| ChunkZ | number | Z-coord of the chunk |
| ChunkDesc | [cChunkDesc](#cChunkDesc) | Generated chunk data. Plugins may still modify the chunk data contained. |

If the plugin returns false or no value, Cuberite will call other plugins' callbacks for this event.
If a plugin returns true, no other callback is called for this event.

In either case, Cuberite will then store the data from ChunkDesc as the chunk's contents in the world.
