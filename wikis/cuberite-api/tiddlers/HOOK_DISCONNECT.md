This hook is called when a client has disconnected from the server, for whatever reason. It is also
called when the client sends the Disconnect packet (only in pre-1.7 protocols). This hook is not called
for server ping connections.

Note that the hook is called even for connections to players who failed to auth. In such a case there's
no {{cPlayer}} object associated with the client.

See also the {{OnHandshake|HOOK_HANDSHAKE}} hook which is called when the client connects (and presents
a handshake message, so that they are not just status-pinging). If you need to store a per-player
object, use the {{OnPlayerJoined|HOOK_PLAYER_JOINED}} and {{OnPlayerDestroyed|HOOK_PLAYER_DESTROYED}}
hooks instead, those are guaranteed to have the {{cPlayer}} object associated.

## Callback function

The default name for the callback function is OnDisconnect. It has the following signature:

```lua
function MyOnDisconnect(Client, Reason)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| Client | [cClientHandle](#cClientHandle) | The client who has disconnected |
| Reason | string | The reason that the client has sent in the disconnect packet |

If the function returns false or no value, Cuberite calls other plugins' callbacks for this event.
If the function returns true, no other plugins are called for this event. In either case,
the client is disconnected.
