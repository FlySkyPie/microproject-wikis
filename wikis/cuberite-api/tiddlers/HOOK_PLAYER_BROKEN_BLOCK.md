This function is called after a {{cPlayer|player}} breaks a block. The block is already removed
from the {{cWorld|world}} and {{cPickup|pickups}} have been spawned. To get the world in which the
block has been dug, use the {{cPlayer}}:GetWorld() function.

See also the {{OnPlayerBreakingBlock|HOOK_PLAYER_BREAKING_BLOCK}} hook for a similar hook called
before the block is broken. To intercept the creation of pickups, see the
{{OnBlockToPickups|HOOK_BLOCK_TO_PICKUPS}} hook.

## Callback function

The default name for the callback function is OnPlayerBrokenBlock. It has the following signature:

```lua
function MyOnPlayerBrokenBlock(Player, BlockX, BlockY, BlockZ, BlockFace, BlockType, BlockMeta)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| Player | [cPlayer](#cPlayer) | The player who broke the block |
| BlockX | number | X-coord of the block |
| BlockY | number | Y-coord of the block |
| BlockZ | number | Z-coord of the block |
| BlockFace | number | Face of the block upon which the player interacted. One of the BLOCK_FACE_ constants |
| BlockType | BLOCKTYPE | The block type of the block |
| BlockMeta | NIBBLETYPE | The block meta of the block |

If the function returns false or no value, the next plugin's callback is called. If the function
returns true, no other callback is called for this event.
