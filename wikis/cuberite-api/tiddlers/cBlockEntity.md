Block entities are simply blocks in the world that have persistent data, such as the text for a sign
or contents of a chest. All block entities are also saved in the chunk data of the chunk they reside in.
The cBlockEntity class acts as a common ancestor for all the individual block entities.

## Functions

### GetBlockType()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| BLOCKTYPE | number |  |

Returns the blocktype which is represented by this blockentity. This is the primary means of type-identification

### GetChunkX()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the chunk X-coord of the block entity's chunk

### GetChunkZ()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the chunk Z-coord of the block entity's chunk

### GetPos()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | Vector3i |  |

Returns the name of the parent class, or empty string if no parent class.

### GetPosX()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the block X-coord of the block entity's block

### GetPosY()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the block Y-coord of the block entity's block

### GetPosZ()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the block Z-coord of the block entity's block

### GetRelPos()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | Vector3i |  |

Returns the relative coords of the block entity's block within its chunk

### GetRelX()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the relative X coord of the block entity's block within the chunk

### GetRelZ()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the relative Z coord of the block entity's block within the chunk

### GetWorld()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | cWorld |  |

Returns the world to which the block entity belongs
