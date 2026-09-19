A plugin may implement a callback for this hook to intercept both in-game commands executed by the
players and console commands executed by the server admin. The function is called for every in-game
command sent from any player and for those server console commands that are not built in in the
server.

If the command is in-game, the first parameter to the hook function is the {{cPlayer|player}} who's
executing the command. If the command comes from the server console, the first parameter is nil.

The server calls this hook even for unregistered (unknown) console commands. It also calls the hook
for unknown in-game commands, as long as they begin with a slash ('/'). If a plugin needs to intercept
in-game chat messages not beginning with a slash, it should use the {{OnChat|HOOK_CHAT}} hook.

## Callback function

The default name for the callback function is OnExecuteCommand. It has the following signature:

```lua
function MyOnExecuteCommand(Player, CommandSplit, EntireCommand)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| Player | [cPlayer](#cPlayer) | For in-game commands, the player who has sent the message. For console commands, nil |
| CommandSplit | array-table of strings | The command and its parameters, broken into a table by spaces |
| EntireCommand | string | The entire command as a single string |

If the plugin returns false, Cuberite calls all the remaining hook handlers and finally the command
will be executed. If the plugin returns true, the none of the remaining hook handlers will be called.
In this case the plugin can return a second value, specifying whether what the command result should
be set to, one of the {{cPluginManager#CommandResult|CommandResult}} constants. If not
provided, the value defaults to crBlocked.
