**Inherits from:** [cBlockEntity](#cBlockEntity)

This class is a common ancestor for all {{cBlockEntity|block entities}} that provide item storage.
Internally, the object has a {{cItemGrid|cItemGrid}} object for storing the items; this ItemGrid is
accessible through the API. The storage is a grid of items, items in it can be addressed either by a slot
number, or by XY coords within the grid. If a UI window is opened for this block entity, the item storage
is monitored for changes and the changes are immediately sent to clients of the UI window.

## Functions

### GetContents()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | cItemGrid |  |

Returns the cItemGrid object representing the items stored within this block entity

### Overload 1: GetSlot(SlotNum)

| Name | Type | Notes |
| --- | --- | --- |
| SlotNum | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | cItem |  |

Returns the cItem for the specified slot number. Returns nil for invalid slot numbers

### Overload 2: GetSlot(X, Y)

| Name | Type | Notes |
| --- | --- | --- |
| X | number |  |
| Y | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | cItem |  |

Returns the cItem for the specified slot coords. Returns nil for invalid slot coords

### Overload 1: SetSlot(SlotNum, cItem)

| Name | Type | Notes |
| --- | --- | --- |
| SlotNum | number |  |
| cItem | cItem |  |

Sets the cItem for the specified slot number. Ignored if invalid slot number

### Overload 2: SetSlot(X, Y, cItem)

| Name | Type | Notes |
| --- | --- | --- |
| X | number |  |
| Y | number |  |
| cItem | cItem |  |

Sets the cItem for the specified slot coords. Ignored if invalid slot coords
