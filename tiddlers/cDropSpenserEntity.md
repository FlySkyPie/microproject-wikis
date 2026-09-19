**Inherits from:** [cBlockEntityWithItems](#cBlockEntityWithItems)

This is a class that implements behavior common to both {{cDispenserEntity|dispensers}} and {{cDropperEntity|droppers}}.

## Functions

### Activate()

Sets the block entity to dropspense an item in the next tick

### AddDropSpenserDir(BlockPos, BlockMeta)

| Name | Type | Notes |
| --- | --- | --- |
| BlockPos | Vector3i |  |
| BlockMeta | number |  |

Adjusts the block coords to where the dropspenser items materialize

## Constants

| Name | Notes |
| --- | --- |
| ContentsHeight | Height (Y) of the {{cItemGrid}} representing the contents |
| ContentsWidth | Width (X) of the {{cItemGrid}} representing the contents |
