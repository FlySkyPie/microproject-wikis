A plugin may implement an OnChat() function and register it as a Hook to process chat messages from
the players. The function is then called for every in-game message sent from any player. Note that
registered in-game commands are not sent through this hook. Use the
{{OnExecuteCommand|HOOK_EXECUTE_COMMAND}} to intercept registered in-game commands.

## Callback function

The default name for the callback function is OnChat. It has the following signature:

```lua
function MyOnChat(Player, Message)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| Player | [cPlayer](#cPlayer) | The player who sent the message |
| Message | string | The message |

The plugin may return 2 values. The first is a boolean specifying whether the hook handling is to be
stopped or not. If it is false, the message is broadcast to all players in the world. If it is true,
no message is broadcast and no further action is taken.

The second value is specifies the message to broadcast. This way, plugins may modify the message. If
the second value is not provided, the original message is used.
