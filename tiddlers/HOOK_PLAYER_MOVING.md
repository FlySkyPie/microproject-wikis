This function is called in each server tick for each {{cPlayer|player}} that has sent any of the
player-move packets. Plugins may refuse the movement.

## Callback function

The default name for the callback function is OnPlayerMoving. It has the following signature:

```lua
function MyOnPlayerMoving(Player, OldPosition, NewPosition, PreviousIsOnGround)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| Player | [cPlayer](#cPlayer) | The player who has moved. The object already has the new position stored in it. |
| OldPosition | [Vector3d](#Vector3d) | The old position. |
| NewPosition | [Vector3d](#Vector3d) | The new position. |
| PreviousIsOnGround | [boolean](#boolean) | Specifies if the player was standing on a solid block. |

If the function returns true, movement is prohibited.

If the function returns false or no value, other plugins' callbacks are called and finally the new
position is permanently stored in the cPlayer object.
