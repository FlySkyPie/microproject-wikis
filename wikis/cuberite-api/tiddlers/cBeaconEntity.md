**Inherits from: **[cBlockEntityWithItems](#cBlockEntityWithItems)

A beacon entity is a {{cBlockEntityWithItems}} descendant that represents a beacon
in the world.

## Functions

### CalculatePyramidLevel()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Calculate the amount of layers the pyramid below the beacon has.

### GetBeaconLevel()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the beacon level. (0 - 4)

### GetPrimaryEffect()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| EffectType | cEntityEffect#eType |  |

Returns the primary effect.

### GetSecondaryEffect()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| EffectType | cEntityEffect#eType |  |

Returns the secondary effect.

### GiveEffects()

Give the near-players the effects.

### IsActive()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Is the beacon active?

### IsBeaconBlocked()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Is the beacon blocked by non-transparent blocks that are higher than the beacon?

### **Static** IsMineralBlock(BlockType)

| Name | Type | Notes |
| --- | --- | --- |
| BlockType | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if the block is a diamond block, a golden block, an iron block or an emerald block.

### **Static** IsValidEffect(EffectType, BeaconLevel)

| Name | Type | Notes |
| --- | --- | --- |
| EffectType | cEntityEffect#eType |  |
| BeaconLevel | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if the effect can be used.

### SetPrimaryEffect(EffectType)

| Name | Type | Notes |
| --- | --- | --- |
| EffectType | cEntityEffect#eType |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Select the primary effect. Returns false when the effect is invalid.

### SetSecondaryEffect(EffectType)

| Name | Type | Notes |
| --- | --- | --- |
| EffectType | cEntityEffect#eType |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Select the secondary effect. Returns false when the effect is invalid.

### UpdateBeacon()

Update the beacon.
