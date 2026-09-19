This callback is called whenever a {{cHopperEntity|hopper}} transfers an {{cItem|item}} from another
block entity into its own internal storage. A plugin may decide to disallow the move by returning
true. Note that in such a case, the hook may be called again for the same hopper, with different
slot numbers.

## Callback function

The default name for the callback function is OnHopperPullingItem. It has the following signature:

```lua
function MyOnHopperPullingItem(World, Hopper, DstSlot, SrcBlockEntity, SrcSlot)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| World | [cWorld](#cWorld) | World where the hopper resides |
| Hopper | [cHopperEntity](#cHopperEntity) | The hopper that is pulling the item |
| DstSlot | number | The destination slot in the hopper's {{cItemGrid|internal storage}} |
| SrcBlockEntity | [cBlockEntityWithItems](#cBlockEntityWithItems) | The block entity that is losing the item |
| SrcSlot | number | Slot in SrcBlockEntity from which the item will be pulled |

If the function returns false or no value, the next plugin's callback is called. If the function
returns true, no other callback is called for this event and the hopper will not pull the item.
