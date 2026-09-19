This hook is called before the server moves the {{cEntity|entity}} to the given world. Plugins may
refuse the changing of the entity to the new world.

See also the {{OnEntityChangedWorld|HOOK_ENTITY_CHANGED_WORLD}} hook for a similar hook is called after the
entity has been moved to the world.

## Callback function

The default name for the callback function is OnEntityChangingWorld. It has the following signature:

```lua
function MyOnEntityChangingWorld(Entity, World)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| Entity | [cEntity](#cEntity) | The entity that wants to change the world |
| World | [cWorld](#cWorld) | The world to which the entity wants to change |

If the function returns false or no value, the next plugin's callback is called. If the function
returns true, no other callback is called for this event and the change of the entity to the world is
cancelled.
