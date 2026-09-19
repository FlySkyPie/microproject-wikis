**Inherits from:** [cDropSpenserEntity](#cDropSpenserEntity)

This class represents a dispenser block entity in the world. Most of this block entity's
functionality is implemented in the {{cDropSpenserEntity}} class that represents
the behavior common with the {{cDropperEntity|dropper}} block entity.

## Functions

### **Static** GetShootVector(BlockMeta)

| Name | Type | Notes |
| --- | --- | --- |
| BlockMeta | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | Vector3d |  |

Returns a unit vector in the cardinal direction of where the dispenser with the specified meta would be facing.

### SpawnProjectileFromDispenser(BlockX, BlockY, BlockZ, Kind, Speed, Item)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockY | number |  |
| BlockZ | number |  |
| Kind | cProjectileEntity#eKind |  |
| Speed | Vector3d |  |
| Item | cItem |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Spawns a projectile of the given kind in front of the dispenser with the specified speed. Returns the UniqueID of the spawned projectile, or {{cEntity#INVALID_ID|cEntity.INVALID_ID}} on failure.
