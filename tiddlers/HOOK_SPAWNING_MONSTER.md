This hook is called before the server spawns a {{cMonster|monster}}. The plugins may modify the
monster's parameters in the {{cMonster}} class, or disallow the spawning altogether. This hook is
called before the {{OnSpawningEntity|HOOK_SPAWNING_ENTITY}} is called for the monster entity.

See also the {{OnSpawnedMonster|HOOK_SPAWNED_MONSTER}} hook for a similar hook called after the
monster is spawned.

## Callback function

The default name for the callback function is OnSpawningMonster. It has the following signature:

```lua
function MyOnSpawningMonster(World, Monster)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| World | [cWorld](#cWorld) | The world in which the entity will spawn |
| Monster | [cMonster](#cMonster) | The monster that will spawn |

If the function returns false or no value, the next plugin's callback is called. Finally, the server
spawns the monster with whatever parameters the plugins set in the cMonster parameter.

If the function returns true, no other callback is called for this event and the monster won't
spawn.
