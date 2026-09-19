This hook is called when a {{cProjectileEntity|projectile}} hits a solid block..

## Callback function

The default name for the callback function is OnProjectileHitBlock. It has the following signature:

```lua
function MyOnProjectileHitBlock(ProjectileEntity, BlockX, BlockY, BlockZ, BlockFace, BlockHitPos)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| ProjectileEntity | [cProjectileEntity](#cProjectileEntity) | The projectile that hit an entity. |
| BlockX | number | The X-coord where the projectile hit. |
| BlockY | number | The Y-coord where the projectile hit. |
| BlockZ | number | The Z-coord where the projectile hit. |
| BlockFace | number | The side of the block where the projectile hit. |
| BlockHitPos | Vector3d | The exact position where the projectile hit. |

If the function returns false or no value, the next plugin's callback is called. If the function
returns true, no other callback is called for this event and the projectile flies through block..
