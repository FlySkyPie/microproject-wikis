This function is called before a {{cPlayer|player}} is about to be destroyed.
The player has disconnected for whatever reason and is no longer in the server.
If a plugin returns true, a leave message is not broadcast, and vice versa.
However, whatever the return value, the player object is removed from memory.

## Callback function

The default name for the callback function is OnPlayerDestroyed. It has the following signature:

```lua
function MyOnPlayerDestroyed(Player)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| Player | [cPlayer](#cPlayer) | The destroyed player |

If the function returns false or no value, other plugins' callbacks are called and a leave message is broadcast.
If the function returns true, no other callbacks are called for this event and no leave message appears. Either way the player is removed internally.
