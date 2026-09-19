This hook is called when a {{cPlayer|player}} has right-clicked a block with an {{cItem|item}} that
can be used (is not placeable, is not food and clicked block is not use-able), such as a bucket or a
hoe. It is called before Cuberite processes the usage (places fluid / turns dirt to farmland).
Plugins may refuse the interaction by returning true.

Note that the block coords given in this callback are for the (solid) block that is being clicked,
not the air block between it and the player.

To get the world at which the right-click occurred, use the {{cPlayer}}:GetWorld() function. To get
the item that the player is using, use the {{cPlayer}}:GetEquippedItem() function.

See also the {{OnPlayerUsedItem|HOOK_PLAYER_USED_ITEM}} for a similar hook called after the use, the
{{OnPlayerUsingBlock|HOOK_PLAYER_USING_BLOCK}} and {{OnPlayerUsedBlock|HOOK_PLAYER_USED_BLOCK}} for
similar hooks called when a player interacts with a block, such as a chest.

## Callback function

The default name for the callback function is OnPlayerUsingItem. It has the following signature:

```lua
function MyOnPlayerUsingItem(Player, BlockX, BlockY, BlockZ, BlockFace, CursorX, CursorY, CursorZ)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| Player | [cPlayer](#cPlayer) | The player who is using the item |
| BlockX | number | X-coord of the clicked block |
| BlockY | number | Y-coord of the clicked block |
| BlockZ | number | Z-coord of the clicked block |
| BlockFace | number | Face of clicked block which has been clicked. One of the BLOCK_FACE_ constants |
| CursorX | number | X-coord of the cursor crosshair on the block being clicked |
| CursorY | number | Y-coord of the cursor crosshair on the block being clicked |
| CursorZ | number | Z-coord of the cursor crosshair on the block being clicked |

If the function returns false or no value, other plugins' callbacks are called and then Cuberite
processes the interaction. If the function returns true, no other callbacks are called for this
event and the interaction is silently dropped.
