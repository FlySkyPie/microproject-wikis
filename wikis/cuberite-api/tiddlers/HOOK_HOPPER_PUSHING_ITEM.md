This hook is called whenever a {{cHopperEntity|hopper}} transfers an {{cItem|item}} from its own
internal storage into another block entity. A plugin may decide to disallow the move by returning
true. Note that in such a case, the hook may be called again for the same hopper and block, with
different slot numbers.

## Callback function

The default name for the callback function is OnHopperPushingItem. It has the following signature:

```lua
function MyOnHopperPushingItem(World, Hopper, SrcSlot, DstBlockEntity, DstSlot)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| World | [cWorld](#cWorld) | World where the hopper resides |
| Hopper | [cHopperEntity](#cHopperEntity) | The hopper that is pushing the item |
| SrcSlot | number | Slot in the hopper that will lose the item |
| DstBlockEntity | [cBlockEntityWithItems](#cBlockEntityWithItems) |  	The block entity that will receive the item |
| DstSlot | number | 	Slot in DstBlockEntity's internal storage where the item will be stored |

If the function returns false or no value, the next plugin's callback is called. If the function
returns true, no other callback is called for this event and the hopper will not push the item.
