This hook is called after the server spawns an {{cEntity|entity}}. This is an information-only
callback, the entity is already spawned by the time it is called. If the entity spawned is a
{{cMonster|monster}}, the {{OnSpawnedMonster|HOOK_SPAWNED_MONSTER}} hook is called before this
hook.

See also the {{OnSpawningEntity|HOOK_SPAWNING_ENTITY}} hook for a similar hook called before the
entity is spawned.

## Callback function

The default name for the callback function is OnSpawnedEntity. It has the following signature:

```lua
function MyOnSpawnedEntity(World, Entity)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| World | [cWorld](#cWorld) | The world in which the entity has spawned |
| Entity | [cEntity](#cEntity) | The entity that has spawned |

If the function returns false or no value, the next plugin's callback is called. If the function
returns true, no other callback is called for this event.
