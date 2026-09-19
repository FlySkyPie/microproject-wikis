This function is called in each server tick for each {{cEntity|Entity}} that has
teleported. Plugins may refuse the teleport.

## Callback function

The default name for the callback function is OnEntityTeleport. It has the following signature:

```lua
function MyOnEntityTeleport(Entity, OldPosition, NewPosition)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| Entity | [cEntity](#cEntity) | The entity who has teleported. New position is set in the object after successfull teleport |
| OldPosition | [Vector3d](#Vector3d) | The old position. |
| NewPosition | [Vector3d](#Vector3d) | The new position. |

If the function returns true, teleport is prohibited.

If the function returns false or no value, other plugins' callbacks are called and finally the new
position is permanently stored in the cEntity object.
