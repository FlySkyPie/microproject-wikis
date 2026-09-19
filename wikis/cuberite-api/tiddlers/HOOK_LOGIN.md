This hook is called whenever a client logs in. It is called right before the client's name is sent
to be authenticated. Plugins may refuse the client from accessing the server. Note that when this
callback is called, the {{cPlayer}} object for this client doesn't exist yet - the client has no
representation in any world. To process new players when their world is known, use a later callback,
such as {{OnPlayerJoined|HOOK_PLAYER_JOINED}} or {{OnPlayerSpawned|HOOK_PLAYER_SPAWNED}}.

## Callback function

The default name for the callback function is OnLogin. It has the following signature:

```lua
function MyOnLogin(Client, ProtocolVersion, UserName)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| Client | [cClientHandle](#cClientHandle) | The client handle representing the connection |
| ProtocolVersion | number | Versio of the protocol that the client is talking |
| UserName | string | The name that the client has presented for authentication. This name will be given to the {{cPlayer}} object when it is created for this client. |

If the function returns true, no other plugins are called for this event and the client is kicked.
If the function returns false or no value, Cuberite calls other plugins' callbacks and finally
sends an authentication request for the client's username to the auth server. If the auth server
is disabled in the server settings, the player object is immediately created.
