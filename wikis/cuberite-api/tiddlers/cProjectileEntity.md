**Inherits from:** [cEntity](#cEntity)

Base class for all projectiles, such as arrows and fireballs.

## Functions

### GetCreatorName()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | string |  |

Returns the name of the player that created the projectile. Will be empty for non-player creators

### GetCreatorUniqueID()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the unique ID of the entity who created this projectile, or {{cEntity#INVALID_ID|cEntity.INVALID_ID}} if the projectile wasn't created by an entity.

### GetMCAClassName()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | string |  |

Returns the string that identifies the projectile type (class name) in MCA files

### GetProjectileKind()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | cProjectileEntity#eKind |  |

Returns the kind of this projectile (pkXXX constant)

### IsInGround()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if this projectile has hit the ground.

## Constants

| Name | Notes |
| --- | --- |
| pkArrow | The projectile is an {{cArrowEntity|arrow}} |
| pkEgg | The projectile is a {{cThrownEggEntity|thrown egg}} |
| pkEnderPearl | The projectile is a {{cThrownEnderPearlEntity|thrown enderpearl}} |
| pkExpBottle | The projectile is a {{cExpBottleEntity|thrown exp bottle}} |
| pkFireCharge | The projectile is a {{cFireChargeEntity|fire charge}} |
| pkFirework | The projectile is a (flying) {{cFireworkEntity|firework}} |
| pkGhastFireball | The projectile is a {{cGhastFireballEntity|ghast fireball}} |
| pkSnowball | The projectile is a {{cThrownSnowballEntity|thrown snowball}} |
| pkSplashPotion | The projectile is a {{cSplashPotionEntity|thrown splash potion}} |
| pkWitherSkull | The projectile is a {{cWitherSkullEntity|wither skull}} |

## Constant Groups

The following constants are used to distinguish between the different projectile kinds:

### eKind
