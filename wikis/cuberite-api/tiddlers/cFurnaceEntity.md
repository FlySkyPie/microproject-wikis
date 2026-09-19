**Inherits from:** [cBlockEntityWithItems](#cBlockEntityWithItems)

This class represents a furnace block entity in the world.

See also {{cRoot}}'s GetFurnaceRecipe() and GetFurnaceFuelBurnTime() functions

## Functions

### GetAndResetReward()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Calculates, resets, and returns the experience reward in this furnace

### GetCookTimeLeft()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the time until the current item finishes cooking, in ticks

### GetFuelBurnTimeLeft()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the time until the current fuel is depleted, in ticks

### GetFuelSlot()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | cItem |  |

Returns the item in the fuel slot

### GetInputSlot()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | cItem |  |

Returns the item in the input slot

### GetOutputSlot()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | cItem |  |

Returns the item in the output slot

### GetTimeCooked()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the time that the current item has been cooking, in ticks

### HasFuelTimeLeft()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if there's time before the current fuel is depleted

### SetFuelSlot(Fuel)

| Name | Type | Notes |
| --- | --- | --- |
| Fuel | cItem |  |

Sets the item in the fuel slot

### SetInputSlot(Input)

| Name | Type | Notes |
| --- | --- | --- |
| Input | cItem |  |

Sets the item in the input slot

### SetOutputSlot(Output)

| Name | Type | Notes |
| --- | --- | --- |
| Output | cItem |  |

Sets the item in the output slot

## Constants

| Name | Notes |
| --- | --- |
| ContentsHeight | Height (Y) of the {{cItemGrid|cItemGrid}} representing the contents |
| ContentsWidth | Width (X) of the {{cItemGrid|cItemGrid}} representing the contents |
| fsFuel | Index of the fuel slot |
| fsInput | Index of the input slot |
| fsOutput | Index of the output slot |

## Constant Groups

When using the GetSlot() or SetSlot() function, use these constants for slot index:

### SlotIndices
