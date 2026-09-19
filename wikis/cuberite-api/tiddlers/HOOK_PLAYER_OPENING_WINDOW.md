This hook is called when a player is about to open a window, e.g. when they click on a chest or a furnace.

## Callback function

The default name for the callback function is OnPlayerOpeningWindow. It has the following signature:

```lua
function MyOnPlayerOpeningWindow(Player, Window)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| Player | [cPlayer](#cPlayer) | The player who is opening the window |
| Window | [cWindow](#cWindow) | The window that is being opened |

If the function returns false or no value, the next plugin's callback is called, and finally
Cuberite will process the opening window. If the function returns true, no other callback is called for this event.
