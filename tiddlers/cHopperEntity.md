**Inherits from:** [cBlockEntityWithItems](#cBlockEntityWithItems)

This class represents a hopper block entity in the world.

## Functions

### GetOutputBlockPos(BlockMeta)

| Name | Type | Notes |
| --- | --- | --- |
| BlockMeta | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| IsAttached | boolean |  |
| BlockX | number |  |
| BlockY | number |  |
| BlockZ | number |  |

Returns whether the hopper is attached, and if so, the block coords of the block receiving the output items, based on the given meta.

## Constants

| Name | Notes |
| --- | --- |
| ContentsHeight | Height (Y) of the internal {{cItemGrid}} representing the hopper contents. |
| ContentsWidth | Width (X) of the internal {{cItemGrid}} representing the hopper contents. |
