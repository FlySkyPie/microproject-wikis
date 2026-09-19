This hook is called after the server spawns a {{cMonster|monster}}. This is an information-only
callback, the monster is already spawned by the time it is called. After this hook is called, the
{{OnSpawnedEntity|HOOK_SPAWNED_ENTITY}} is called for the monster entity.

See also the {{OnSpawningMonster|HOOK_SPAWNING_MONSTER}} hook for a similar hook called before the
monster is spawned.

## Callback function

The default name for the callback function is OnSpawnedMonster. It has the following signature:

```lua
function MyOnSpawnedMonster(World, Monster)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| World | [cWorld](#cWorld) | The world in which the monster has spawned |
| Monster | [cMonster](#cMonster) | The monster that has spawned |

If the function returns false or no value, the next plugin's callback is called. If the function
returns true, no other callback is called for this event.
