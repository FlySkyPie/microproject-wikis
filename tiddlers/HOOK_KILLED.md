This hook is called whenever player or a mob dies. It can be used to change the death message.

## Callback function

The default name for the callback function is OnKilled. It has the following signature:

```lua
function MyOnKilled(Victim, TDI, DeathMessage)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| Victim | [cEntity](#cEntity) | The player or mob that died |
| TDI | [TakeDamageInfo](#TakeDamageInfo) | Informations about the death |
| DeathMessage | string | The default death message. An empty string if the victim is not a player |

The function may return two values. The first value is a boolean specifying whether other plugins should be called. If it is true, the other plugins won't get notified of the death. If it is false, the other plugins will get notified.

The second value is a string containing the death message. If the victim is a player, this death message is broadcasted instead of the default death message. If it is empty, no death message is broadcasted. If it is nil, the message is left unchanged. If the victim is not a player, the death message is never broadcasted.

In either case, the victim is dead.
