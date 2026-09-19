This hook is called after a {{cPlayer|player}} has placed a block in the {{cWorld|world}}. The block
is already added to the world and the corresponding item removed from player's
{{cInventory|inventory}}.

Use the {{cPlayer}}:GetWorld() function to get the world to which the block belongs.

See also the {{OnPlayerPlacingBlock|HOOK_PLAYER_PLACING_BLOCK}} hook for a similar hook called
before the placement.

If the client action results in multiple blocks being placed (such as a bed or a door), each separate
block is reported through this hook. All the blocks are already present in the world before the first
instance of this hook is called.

## Callback function

The default name for the callback function is OnPlayerPlacedBlock. It has the following signature:

```lua
function MyOnPlayerPlacedBlock(Player, BlockX, BlockY, BlockZ, BlockType, BlockMeta)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| Player | [cPlayer](#cPlayer) | The player who placed the block |
| BlockX | number | X-coord of the block |
| BlockY | number | Y-coord of the block |
| BlockZ | number | Z-coord of the block |
| BlockType | BLOCKTYPE | The block type of the block |
| BlockMeta | NIBBLETYPE | The block meta of the block |

If this function returns false or no value, Cuberite calls other plugins with the same event. If
this function returns true, no other plugin is called for this event.
