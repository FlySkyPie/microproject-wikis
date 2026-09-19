**Inherits from:** [cBlockEntity](#cBlockEntity)

This class represents a mob head block entity in the world.

## Functions

### GetOwnerName()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | string |  |

Returns the player name of the mob head

### GetOwnerTexture()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | string |  |

Returns the player texture of the mob head

### GetOwnerTextureSignature()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | string |  |

Returns the signature of the player texture of the mob head

### GetOwnerUUID()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | string |  |

Returns the player UUID of the mob head

### GetRotation()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | eMobHeadRotation |  |

Returns the rotation of the mob head

### GetType()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | eMobHeadType |  |

Returns the type of the mob head

### Overload 1: SetOwner(cPlayer)

| Name | Type | Notes |
| --- | --- | --- |
| cPlayer | cPlayer |  |

Set the {{cPlayer|player}} for mob heads with player type

### Overload 2: SetOwner(OwnerUUID, OwnerName, OwnerTexture, OwnerTextureSignature)

| Name | Type | Notes |
| --- | --- | --- |
| OwnerUUID | string |  |
| OwnerName | string |  |
| OwnerTexture | string |  |
| OwnerTextureSignature | string |  |

Sets the player components for the mob heads with player type

### SetRotation(Rotation)

| Name | Type | Notes |
| --- | --- | --- |
| Rotation | eMobHeadRotation |  |

Sets the rotation of the mob head.

### SetType(HeadType)

| Name | Type | Notes |
| --- | --- | --- |
| HeadType | eMobHeadType |  |

Set the type of the mob head
