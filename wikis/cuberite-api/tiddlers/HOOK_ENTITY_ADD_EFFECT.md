This hook is called whenever an entity effect is about to be added to an entity. The plugin may
disallow the addition by returning true.

Note that this hook only fires for adding the effect, but not for the actual effect application. See
also the {{OnEntityRemoveEffect|HOOK_ENTITY_REMOVE_EFFECT}} for notification about effects expiring /
removing, and {{OnEntityApplyEffect|HOOK_ENTITY_APPLY_EFFECT}} for the actual effect application to the
entity.

## Callback function

The default name for the callback function is OnEntityAddEffect. It has the following signature:

```lua
function MyOnEntityAddEffect(Entity, EffectType, EffectDuration, EffectIntensity, DistanceModifier)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| Entity | [cEntity](#cEntity) | The entity to which the effect is about to be added |
| EffectType | number | The type of the effect to be added. One of the effXXX constants. |
| EffectDuration | number | The duration of the effect to be added, in ticks. |
| EffectIntensity | number | The intensity (level) of the effect to be added.  |
| DistanceModifier | number | The modifier for the effect intensity, based on distance. Used mainly for splash potions. |

If the plugin returns true, the effect will not be added and none of the remaining hook handlers will
be called. If the plugin returns false, Cuberite calls all the remaining hook handlers and finally
the effect is added to the entity.
