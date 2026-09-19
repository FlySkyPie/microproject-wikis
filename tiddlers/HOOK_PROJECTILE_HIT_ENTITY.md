This hook is called when a {{cProjectileEntity|projectile}} hits another entity.

## Callback function

The default name for the callback function is OnProjectileHitEntity. It has the following signature:

```lua
function MyOnProjectileHitEntity(ProjectileEntity, Entity)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| ProjectileEntity | [cProjectileEntity](#cProjectileEntity) | The projectile that hit an entity. |
| Entity | [cEntity](#cEntity) | The entity wich was hit. |

If the function returns false or no value, the next plugin's callback is called. If the function
returns true, no other callback is called for this event and the projectile flies through the entity.
