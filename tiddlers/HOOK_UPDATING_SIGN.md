This hook is called when a sign text is about to be updated, either as a result of player's
manipulation or any other event, such as a plugin setting the sign text. Plugins may modify the text
or refuse the update altogether.

See also the {{OnUpdatedSign|HOOK_UPDATED_SIGN}} hook for a similar hook called after the update.

## Callback function

The default name for the callback function is OnUpdatingSign. It has the following signature:

```lua
function MyOnUpdatingSign(World, BlockX, BlockY, BlockZ, Line1, Line2, Line3, Line4, Player)
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

The function may return up to five values. If the function returns true as the first value, no other
callbacks are called for this event and the sign is not updated. If the function returns no value or
false as its first value, other plugins' callbacks are called.

The other up to four values returned are used to update the sign text, line by line, respectively.
Note that other plugins may again update the texts (if the first value returned is false).
