This hook is called whenever a {{cPlayer|player}} has completely logged in. If authentication is
enabled, this function is called after their name has been authenticated. It is called after
{{OnLogin|HOOK_LOGIN}} and before {{OnPlayerSpawned|HOOK_PLAYER_SPAWNED}}, right after the player's
entity is created, but not added to the world yet. The player is not yet visible to other players.
Returning true will block a join message from being broadcast, but otherwise, the player is still allowed to join.
Plugins wishing to refuse player's entry should kick the player using the {{cPlayer}}:Kick() function.

## Callback function

The default name for the callback function is OnPlayerJoined. It has the following signature:

```lua
function MyOnPlayerJoined(Player)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| Player | [cPlayer](#cPlayer) | The player who has joined the game |

If the function returns false or no value, other plugins' callbacks are called and a join message is broadcast. If the function
returns true, no other callbacks are called for this event and a join message is not sent. Either way the player is let in.
