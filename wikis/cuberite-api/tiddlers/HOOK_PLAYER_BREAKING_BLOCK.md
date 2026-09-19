This hook is called when a {{cPlayer|player}} breaks a block, before the block is actually broken in
the {{cWorld|World}}. Plugins may refuse the breaking.

See also the {{OnPlayerBrokenBlock|HOOK_PLAYER_BROKEN_BLOCK}} hook for a similar hook called after
the block is broken.

## Callback function

The default name for the callback function is OnPlayerBreakingBlock. It has the following signature:

```lua
function MyOnPlayerBreakingBlock(Player, BlockX, BlockY, BlockZ, BlockFace, BlockType, BlockMeta)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| Player | [cPlayer](#cPlayer) | The player who is digging the block |
| BlockX | number | X-coord of the block |
| BlockY | number | Y-coord of the block |
| BlockZ | number | Z-coord of the block |
| BlockFace | number | Face of the block upon which the player is acting. One of the BLOCK_FACE_ constants |
| BlockType | BLOCKTYPE | The block type of the block being broken |
| BlockMeta | NIBBLETYPE | The block meta of the block being broken  |

If the function returns false or no value, other plugins' callbacks are called, and then the block
is broken. If the function returns true, no other plugin's callback is called and the block breaking
is cancelled. The server re-sends the block back to the player to replace it (the player's client
already thinks the block was broken).
