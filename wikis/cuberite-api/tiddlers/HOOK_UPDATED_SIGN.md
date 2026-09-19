This hook is called after a sign has had its text updated. The text is already updated at this
point.

The update may have been caused either by a {{cPlayer|player}} directly updating the sign, or by
a plugin changing the sign text using the API.

See also the {{OnUpdatingSign|HOOK_UPDATING_SIGN}} hook for a similar hook called before the update,
with a chance to modify the text.

## Callback function

The default name for the callback function is OnUpdatedSign. It has the following signature:

```lua
function MyOnUpdatedSign(World, BlockX, BlockY, BlockZ, Line1, Line2, Line3, Line4, Player)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| World | [cWorld](#cWorld) | The world in which the sign resides |
| BlockX | number | X-coord of the sign |
| BlockY | number | Y-coord of the sign |
| BlockZ | number | Z-coord of the sign |
| Line1 | string | 1st line of the new text |
| Line2 | string | 2nd line of the new text |
| Line3 | string | 3rd line of the new text |
| Line4 | string | 4th line of the new text |
| Player | [cPlayer](#cPlayer) | The player who is changing the text. May be nil for non-player updates. |

If the function returns false or no value, other plugins' callbacks are called. If the function
returns true, no other callbacks are called. There is no overridable behavior.
