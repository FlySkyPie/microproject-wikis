This hook gets called when a player right clicks with a fishing rod while the floater is under water. The reward is already descided, but the plugin may change it.

## Callback function

The default name for the callback function is OnPlayerFishing. It has the following signature:

```lua
function MyOnPlayerFishing(Player, Reward)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| Player | [cPlayer](#cPlayer) | The player who pulled the fish in. |
| Reward | [cItems](#cItems) | The reward the player gets. It can be a fish, treasure and junk. |

If the function returns false or no value, the next plugin's callback is called. Afterwards, the
server gives the player his reward. If the function returns true, no other
callback is called for this event and the player doesn't get his reward.
