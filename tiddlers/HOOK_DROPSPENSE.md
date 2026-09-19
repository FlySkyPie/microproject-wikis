This callback is called whenever a {{cDropSpenserEntity|dropspenser}} dropspenses an {{cItem|item}}. A plugin may decide to disallow
the move by returning true.

## Callback function

The default name for the callback function is OnDropSpense. It has the following signature:

```lua
function MyOnDropSpense(World, DropSpenser, SlotNum)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| World | [cWorld](#cWorld) | World where the dropspenser resides |
| DropSpenser | [cDropSpenserEntity](#cDropSpenserEntity) | The dropspenser that is pulling the item |
| SlotNum | number | The slot of the dropspensed item in the dropspenser's {{cItemGrid|internal storage}} |

If the function returns false or no value, the next plugin's callback is called. If the function
returns true, no other callback is called for this event and the dropspenser will not dropspense the item.
