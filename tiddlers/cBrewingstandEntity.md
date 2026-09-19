**Inherits from:** [cBlockEntityWithItems](#cBlockEntityWithItems)

This class represents a brewingstand entity in the world.

See also the {{cRoot}}:GetBrewingRecipe() function.

## Functions

### GetBrewingTimeLeft()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the time until the current items finishes brewing, in ticks

### GetFuelSlot()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | cItem |  |

Returns the item in the top left fuel slot

### GetIndgredientSlot()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | cItem |  |

Returns the item in the ingredient slot

### GetLeftBottleSlot()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | cItem |  |

Returns the item in the left bottle slot

### GetMiddleBottleSlot()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | cItem |  |

Returns the item in the middle bottle slot

### GetRemainingFuel()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the remaining fuel that is left. It's the amount of brewing operations that can be done (20 for one blaze powder).

### GetResultItem(SlotNumber)

| Name | Type | Notes |
| --- | --- | --- |
| SlotNumber | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | cItem |  |

Returns the expected result item for the given slot number.

### GetRightBottleSlot()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | cItem |  |

Returns the item in the right bottle slot

### GetTimeBrewed()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the time that the current items has been brewing, in ticks

### SetFuelSlot(FuelSlot)

| Name | Type | Notes |
| --- | --- | --- |
| FuelSlot | cItem |  |

Sets the item in the top left fuel slot

### SetIngredientSlot(Ingredient)

| Name | Type | Notes |
| --- | --- | --- |
| Ingredient | cItem |  |

Sets the item in the ingredient bottle slot

### SetLeftBottleSlot(LeftSlot)

| Name | Type | Notes |
| --- | --- | --- |
| LeftSlot | cItem |  |

Sets the item in the left bottle slot

### SetMiddleBottleSlot(MiddleSlot)

| Name | Type | Notes |
| --- | --- | --- |
| MiddleSlot | cItem |  |

Sets the item in the middle bottle slot

### SetRightBottleSlot(RightSlot)

| Name | Type | Notes |
| --- | --- | --- |
| RightSlot | cItem |  |

Sets the item in the right bottle slot

## Constants

| Name | Notes |
| --- | --- |
| ContentsHeight | Height (Y) of the {{cItemGrid|cItemGrid}} representing the contents |
| ContentsWidth | Width (X) of the {{cItemGrid|cItemGrid}} representing the contents |
| bsFuel | Index of the top left fuel slot |
| bsIngredient | Index of the ingredient slot |
| bsLeftBottle | Index of the left bottle slot |
| bsMiddleBottle | Index of the middle bottle slot |
| bsRightBottle | Index of the right bottle slot |

## Constant Groups

When using the GetSlot() or SetSlot() function, use these constants for slot index:

### SlotIndices
