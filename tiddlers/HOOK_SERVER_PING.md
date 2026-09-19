A plugin may implement an OnServerPing() function and register it as a Hook to process pings from
clients in the server server list. It can change the logged in players and player capacity, as well
as the server description and the favicon, that are displayed to the client in the server list.

The client handle already has its protocol version assigned to it, so the plugin can check that; however,
there's no username associated with the client yet, and no player object.

## Callback function

The default name for the callback function is OnServerPing. It has the following signature:

```lua
function MyOnServerPing(ClientHandle, ServerDescription, OnlinePlayersCount, MaxPlayersCount, Favicon)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| ClientHandle | [cClientHandle](#cClientHandle) | The client handle that pinged the server |
| ServerDescription | string | The server description |
| OnlinePlayersCount | number | The number of players currently on the server |
| MaxPlayersCount | number | The current player cap for the server |
| Favicon | string | The base64 encoded favicon to be displayed in the server list for compatible clients |

The plugin can return whether to continue processing of the hook with other plugins, the server description to
be displayed to the client, the currently online players, the player cap and the base64/png favicon data, in that order.
