This hook gets called after a player reels in the fishing rod. This is a notification-only hook, the reward has already been decided. If a plugin needs to modify the reward, use the {{OnPlayerFishing|HOOK_PLAYER_FISHING}} hook.

## Callback function

The default name for the callback function is OnPlayerFished. It has the following signature:

```lua
function MyOnPlayerFished(Player, Reward)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| Player | [cPlayer](#cPlayer) | The player who pulled the fish in. |
| Reward | [cItems](#cItems) | The reward the player gets. It can be a fish, treasure and junk. |

If the function returns false or no value, the next plugin's callback is called. If the function returns true, no other
callback is called for this event.
