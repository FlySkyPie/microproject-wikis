This hook is called after the server has moved the {{cEntity|entity}} to the given world. This is an information-only
callback, the entity is already in the new world.

See also the {{OnEntityChangingWorld|HOOK_ENTITY_CHANGING_WORLD}} hook for a similar hook called before the
entity is moved to the new world.

## Callback function

The default name for the callback function is OnEntityChangedWorld. It has the following signature:

```lua
function MyOnEntityChangedWorld(Entity, World)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| Entity | [cEntity](#cEntity) | The entity that has changed the world |
| World | [cWorld](#cWorld) | The world from which the entity has come |

If the function returns false or no value, the next plugin's callback is called. If the function
returns true, no other callback is called for this event.
