This hook is called before the world generator starts generating a chunk. The plugin may provide
some or all parts of the generation, by-passing the built-in generator. The function is given access
to the {{cChunkDesc|ChunkDesc}} object representing the contents of the chunk. It may override parts
of the built-in generator by using the object's  functions. After all
the callbacks for a chunk have been processed, the server will generate the chunk based on the
{{cChunkDesc|ChunkDesc}} description - those parts that are set for generating (by default
everything) are generated, the rest are read from the ChunkDesc object.

See also the {{OnChunkGenerated|HOOK_CHUNK_GENERATED}} hook.

## Callback function

The default name for the callback function is OnChunkGenerating. It has the following signature:

```lua
function MyOnChunkGenerating(World, ChunkX, ChunkZ, ChunkDesc)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| World | [cWorld](#cWorld) | The world to which the chunk will be added |
| ChunkX | number | X-coord of the chunk |
| ChunkZ | number | Z-coord of the chunk |
| ChunkDesc | [cChunkDesc](#cChunkDesc) | Generated chunk data. |

If this function returns true, the server will not call any other plugin with the same chunk. If
this function returns false, the server will call the rest of the plugins with the same chunk,
possibly overwriting the ChunkDesc's contents.
