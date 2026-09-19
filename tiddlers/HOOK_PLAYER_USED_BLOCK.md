This hook is called after a {{cPlayer|player}} has right-clicked a block that can be used, such as a
{{cChestEntity|chest}} or a lever. It is called after Cuberite processes the usage (sends the UI
handling packets / toggles redstone). Note that for UI-related blocks, the player is most likely
still using the UI. This is a notification-only event.

Note that the block coords given in this callback are for the (solid) block that is being clicked,
not the air block between it and the player.

To get the world at which the right-click occurred, use the {{cPlayer}}:GetWorld() function.

See also the {{OnPlayerUsingBlock|HOOK_PLAYER_USING_BLOCK}} for a similar hook called before the
use, the {{OnPlayerUsingItem|HOOK_PLAYER_USING_ITEM}} and {{OnPlayerUsedItem|HOOK_PLAYER_USED_ITEM}}
for similar hooks called when a player interacts with any block with a usable item in hand, such as
a bucket.

## Callback function

The default name for the callback function is OnPlayerUsedBlock. It has the following signature:

```lua
function MyOnPlayerUsedBlock(Player, BlockX, BlockY, BlockZ, BlockFace, CursorX, CursorY, CursorZ, BlockType, BlockMeta)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| Player | [cPlayer](#cPlayer) | The player who used the block |
| BlockX | number | X-coord of the clicked block |
| BlockY | number | Y-coord of the clicked block |
| BlockZ | number | Z-coord of the clicked block |
| BlockFace | number | Face of clicked block which has been clicked. One of the BLOCK_FACE_ constants |
| CursorX | number | X-coord of the cursor crosshair on the block being clicked |
| CursorY | number | Y-coord of the cursor crosshair on the block being clicked |
| CursorZ | number | Z-coord of the cursor crosshair on the block being clicked |
| BlockType | number | Block type of the clicked block |
| BlockMeta | number | Block meta of the clicked block |

If the function returns false or no value, other plugins' callbacks are called. If the function
returns true, no other callbacks are called for this event.
