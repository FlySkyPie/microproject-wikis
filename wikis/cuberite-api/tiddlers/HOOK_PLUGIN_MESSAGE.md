A plugin may implement an OnPluginMessage() function and register it as a Hook to process plugin messages
from the players. The function is then called for every plugin message sent from any player.

## Callback function

The default name for the callback function is OnPluginMessage. It has the following signature:

```lua
function MyOnPluginMessage(Client, Channel, Message)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| Client | [cClientHandle](#cClientHandle) | The client who sent the plugin message |
| Channel | string | The channel on which the message was sent |
| Message | string | The message's payload |

If the function returns false or no value, other plugins' callbacks are called. If the function
returns true, no other callbacks are called for this event.
