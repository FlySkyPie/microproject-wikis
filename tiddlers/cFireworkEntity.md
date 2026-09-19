**Inherits from:** [cProjectileEntity](#cProjectileEntity)

Represents a firework rocket.

## Functions

### GetItem()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | cItem |  |

Returns the item that has been used to create the firework rocket. The item's m_FireworkItem member contains all the firework-related data.

### GetTicksToExplosion()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the number of ticks left until the firework explodes.

### SetItem(FireworkItem)

| Name | Type | Notes |
| --- | --- | --- |
| FireworkItem | cItem |  |

Sets a new item to be used for the firework.

### SetTicksToExplosion(NumTicks)

| Name | Type | Notes |
| --- | --- | --- |
| NumTicks | number |  |

Sets the number of ticks left until the firework explodes.
