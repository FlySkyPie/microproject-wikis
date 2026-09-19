This hook is called after a {{cPlayer|player}} has spawned in the world. It is called after
{{OnLogin|HOOK_LOGIN}} and {{OnPlayerJoined|HOOK_PLAYER_JOINED}}, after the player name has been
authenticated, the initial worldtime, inventory and health have been sent to the player and the
player spawn packet has been broadcast to all players near enough to the player spawn place. This is
a notification-only event, plugins wishing to refuse player's entry should kick the player using the
{{cPlayer}}:Kick() function.

This hook is also called when the player respawns after death (and a respawn packet is received from
the client, meaning the player has already clicked the Respawn button).

## Callback function

The default name for the callback function is OnPlayerSpawned. It has the following signature:

```lua
function MyOnPlayerSpawned(Player)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| Player | [cPlayer](#cPlayer) | The player who has (re)spawned |

If the function returns false or no value, other plugins' callbacks are called. If the function
returns true, no other callbacks are called for this event. There is no overridable behavior.
