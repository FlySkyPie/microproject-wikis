This hook is called before the food level changes.
The food level is not changed yet, plugins may choose
to refuse the change.

## Callback function

The default name for the callback function is OnPlayerFoodLevelChange. It has the following signature:

```lua
function MyOnPlayerFoodLevelChange(Player, NewFoodLevel)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| Player | [cPlayer](#cPlayer) | The player who changes the food level. |
| NewFoodLevel | number | The new food level. |

If the function returns false or no value, the next plugin's callback is called. Afterwards, the
server changes the food level of the player. If the function returns true, no
other callback is called for this event and the player's food level doesn't change.
