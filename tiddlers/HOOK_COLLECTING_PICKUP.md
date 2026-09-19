This hook is called when a player is about to collect a pickup. Plugins may refuse the action.

Pickup collection happens within the world tick, so if the collecting is refused, it will be tried
again in the next world tick, as long as the player is within reach of the pickup.

FIXME: There is no OnCollectedPickup() callback.

FIXME: This callback is called even if the pickup doesn't fit into the player's inventory.

## Callback function

The default name for the callback function is OnCollectingPickup. It has the following signature:

```lua
function MyOnCollectingPickup(Player, Pickup)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| Player | [cPlayer](#cPlayer) | The player who's collecting the pickup |
| Pickup | [cPickup](#cPickup) | The pickup being collected |

If the function returns false or no value, Cuberite calls other plugins' callbacks and finally the
pickup is collected. If the function returns true, no other plugins are called for this event and
the pickup is not collected.
