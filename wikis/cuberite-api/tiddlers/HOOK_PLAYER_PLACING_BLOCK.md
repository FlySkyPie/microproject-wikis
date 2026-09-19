This hook is called just before a {{cPlayer|player}} places a block in the {{cWorld|world}}. The
block is not yet placed, plugins may choose to override the default behavior or refuse the placement
at all.

Note that the client already expects that the block has been placed. For that reason, if a plugin
refuses the placement, Cuberite sends the old block at the provided coords to the client.

Use the {{cPlayer}}:GetWorld() function to get the world to which the block belongs.

See also the {{OnPlayerPlacedBlock|HOOK_PLAYER_PLACED_BLOCK}} hook for a similar hook called after
the placement.

If the client action results in multiple blocks being placed (such as a bed or a door), each separate
block is reported through this hook and only if all of them succeed, all the blocks are placed. If
any one of the calls are refused by the plugin, all the blocks are refused and reverted on the client.

## Callback function

The default name for the callback function is OnPlayerPlacingBlock. It has the following signature:

```lua
function MyOnPlayerPlacingBlock(Player, BlockX, BlockY, BlockZ, BlockType, BlockMeta)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| Player | [cPlayer](#cPlayer) | The player who is placing the block |
| BlockX | number | X-coord of the block |
| BlockY | number | Y-coord of the block |
| BlockZ | number | Z-coord of the block |
| BlockType | BLOCKTYPE | The block type of the block |
| BlockMeta | NIBBLETYPE | The block meta of the block |

If this function returns false or no value, Cuberite calls other plugins with the same event and
finally places the block and removes the corresponding item from player's inventory. If this
function returns true, no other plugin is called for this event, Cuberite sends the old block at
the specified coords to the client and drops the packet.
