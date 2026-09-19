This hook is called before the server spawns an {{cEntity|entity}}. The plugin can either modify the
entity before it is spawned, or disable the spawning altogether. You can't disable the spawning if the
entity is a player. If the entity spawning is a monster, the {{OnSpawningMonster|HOOK_SPAWNING_MONSTER}}
hook is called before this hook.

See also the {{OnSpawnedEntity|HOOK_SPAWNED_ENTITY}} hook for a similar hook called after the
entity is spawned.

## Callback function

The default name for the callback function is OnSpawningEntity. It has the following signature:

```lua
function MyOnSpawningEntity(World, Entity)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| World | [cWorld](#cWorld) | The world in which the entity will spawn |
| Entity | [cEntity](#cEntity) | The entity that will spawn |

If the function returns false or no value, the next plugin's callback is called. Finally, the server
spawns the entity with whatever parameters have been set on the {{cEntity}} object by the callbacks.
If the function returns true, no other callback is called for this event and the entity is not
spawned.
