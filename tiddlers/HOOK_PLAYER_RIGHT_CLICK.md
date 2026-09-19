This hook is called when Cuberite receives a right-click packet from the {{cClientHandle|client}}. It
is called before any processing whatsoever is performed on the packet, meaning that hacked /
malicious clients may be trigerring this event very often and with unchecked parameters. Therefore
plugin authors are advised to use extreme caution with this callback.

Plugins may refuse the default processing for the packet, causing Cuberite to behave as if the
packet has never arrived. This may, however, create inconsistencies in the client - the client may
think that they placed a block, while the server didn't process the placing, etc.

## Callback function

The default name for the callback function is OnPlayerRightClick. It has the following signature:

```lua
function MyOnPlayerRightClick(Player, BlockX, BlockY, BlockZ, BlockFace, CursorX, CursorY, CursorZ)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| Player | [cPlayer](#cPlayer) | The player whose client sent the packet |
| BlockX | number | X-coord of the block |
| BlockY | number | Y-coord of the block |
| BlockZ | number | Z-coord of the block |
| BlockFace | number | Face of the block upon which the player interacted. One of the BLOCK_FACE_ constants |
| CursorX | number | X-coord of the mouse crosshair on the block |
| CursorY | number | Y-coord of the mouse crosshair on the block |
| CursorZ | number | Z-coord of the mouse crosshair on the block |

If the function returns false or no value, Cuberite calls other plugins' callbacks and finally sends
the packet for further processing.

If the function returns true, no other plugins are called, processing is halted.
