This hook is called when a client sends the Handshake packet. At this stage, only the client IP and
(unverified) username are known. Plugins may refuse access to the server based on this
information.

Note that the username is not authenticated - the authentication takes place only after this hook is
processed.

## Callback function

The default name for the callback function is OnHandshake. It has the following signature:

```lua
function MyOnHandshake(Client, UserName)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| Client | [cClientHandle](#cClientHandle) | The client handle representing the connection. Note that there's no {{cPlayer}} object for this client yet. |
| UserName | string | The username presented in the packet. Note that this username is unverified. |

If the function returns false, the user is let in to the server. If the function returns true, no
other plugin's callback is called, the user is kicked and the connection is closed.
