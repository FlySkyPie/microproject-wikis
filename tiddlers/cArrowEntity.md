**Inherits from: **[cProjectileEntity](#cProjectileEntity)

Represents the arrow when it is shot from the bow. A subclass of the {{cProjectileEntity}}.

## Functions

### CanPickup(Player)

| Name | Type | Notes |
| --- | --- | --- |
| Player | cPlayer |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if the specified player can pick the arrow when it's on the ground

### GetBlockHit()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | Vector3i |  |

Returns the coords of the block into which the arrow is stuck. Undefined if the arrow is still moving.

### GetDamageCoeff()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the damage coefficient stored within the arrow. The damage dealt by this arrow is multiplied by this coeff

### GetPickupState()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | cArrowEntity#ePickupState |  |

Returns the pickup state (one of the psXXX constants, above)

### IsCritical()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if the arrow should deal critical damage. Based on the bow charge when the arrow was shot.

### SetDamageCoeff(DamageCoeff)

| Name | Type | Notes |
| --- | --- | --- |
| DamageCoeff | number |  |

Sets the damage coefficient. The damage dealt by this arrow is multiplied by this coeff

### SetIsCritical(IsCritical)

| Name | Type | Notes |
| --- | --- | --- |
| IsCritical | boolean |  |

Sets the IsCritical flag on the arrow. Critical arrow deal additional damage

### SetPickupState(PickupState)

| Name | Type | Notes |
| --- | --- | --- |
| PickupState | cArrowEntity#ePickupState |  |

Sets the pickup state (one of the psXXX constants, above)

## Constants

| Name | Notes |
| --- | --- |
| psInCreative | The arrow can be picked up only by players in creative gamemode |
| psInSurvivalOrCreative | The arrow can be picked up by players in survival or creative gamemode |
| psNoPickup | The arrow cannot be picked up at all |

## Constant Groups


					The following constants are used to signalize whether the arrow, once it lands, can be picked by
					players:
				

### ePickupState
