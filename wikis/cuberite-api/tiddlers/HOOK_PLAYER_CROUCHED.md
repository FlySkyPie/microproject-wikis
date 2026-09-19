This function is called in each server tick for each {{cPlayer|player}} that has crouched.

## Callback function

The default name for the callback function is OnPlayerCrouched. It has the following signature:

```lua
function MyOnPlayerCrouched(Player)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| Player | [cPlayer](#cPlayer) | The player who has crouched. |

If the function returns false or no value, other plugins callbacks are called.
