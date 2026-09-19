This hook gets called when the {{cPlayer|player}} starts eating, after the server checks that the
player can indeed eat (is not satiated and is holding food). Plugins may still refuse the eating by
returning true.

## Callback function

The default name for the callback function is OnPlayerEating. It has the following signature:

```lua
function MyOnPlayerEating(Player)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| Player | [cPlayer](#cPlayer) | The player who started eating |

If the function returns false or no value, the server calls the next plugin handler, and finally
lets the player eat. If the function returns true, the server doesn't call any more callbacks for
this event and aborts the eating. A "disallow" packet is sent to the client.
