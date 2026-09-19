This class is used when multiple adjacent blocks are to be manipulated. Because of chunking
and multithreading, manipulating single blocks using {{cWorld|cWorld:SetBlock}}() is a rather
time-consuming operation (locks for exclusive access need to be obtained, chunk lookup is done
for each block), so whenever you need to manipulate multiple adjacent blocks, it's better to wrap
the operation into a cBlockArea access. cBlockArea is capable of reading / writing across chunk
boundaries, has no chunk lookups for get and set operations and is not subject to multithreading
locking (because it is not shared among threads).

cBlockArea remembers its origin (MinX, MinY, MinZ coords in the Read() call) and therefore supports
absolute as well as relative get / set operations. Despite that, the contents of a cBlockArea can
be written back into the world at any coords. Most functions in this class come in pair, one that
works with the absolute coords (what the coords would have been in the original world the area was read
from) and one (usually with "Rel" in their name) that work on the relative coords (those range from
zero to Size - 1). Also note that most functions will raise an error if an out-of-range coord is
supplied to them.

cBlockArea can hold any combination of the following datatypes:

- block types

- block metas

- blocklight

- skylight

- block entities (only together with block types)

Read() and Write() functions have parameters that tell the class which datatypes to read / write.
Note that a datatype that has not been read cannot be written.

Block entities stored inside a cBlockArea object have their position set to the relative position
within the area.

Typical usage:

- Create cBlockArea object

- Read an area from the world / load from file / create anew

- Modify blocks inside cBlockArea

- Write the area back to a world / save to file

Calls to any setter of this class will not trigger simulator updates (lava, water, redstone).

## Functions

### Clear()

Clears the object, resets it to zero size

### CopyFrom(BlockAreaSrc)

| Name | Type | Notes |
| --- | --- | --- |
| BlockAreaSrc | cBlockArea |  |

Copies contents from BlockAreaSrc into self

### CopyTo(BlockAreaDst)

| Name | Type | Notes |
| --- | --- | --- |
| BlockAreaDst | cBlockArea |  |

Copies contents from self into BlockAreaDst.

### CountNonAirBlocks()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the count of blocks that are not air. Returns 0 if blocktypes not available. Block metas are ignored (if present, air with any meta is still considered air).

### Overload 1: CountSpecificBlocks(BlockType)

| Name | Type | Notes |
| --- | --- | --- |
| BlockType | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Counts the number of occurences of the specified blocktype contained in the area.

### Overload 2: CountSpecificBlocks(BlockType, BlockMeta)

| Name | Type | Notes |
| --- | --- | --- |
| BlockType | number |  |
| BlockMeta | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Counts the number of occurrences of the specified blocktype + blockmeta combination contained in the area.

### Overload 1: Create(SizeX, SizeY, SizeZ)

| Name | Type | Notes |
| --- | --- | --- |
| SizeX | number |  |
| SizeY | number |  |
| SizeZ | number |  |

Initializes this BlockArea to an empty area of the specified size and origin of {0, 0, 0}. Datatypes are set to baTypes + baMetas. Any previous contents are lost.

### Overload 2: Create(SizeX, SizeY, SizeZ, DataTypes)

| Name | Type | Notes |
| --- | --- | --- |
| SizeX | number |  |
| SizeY | number |  |
| SizeZ | number |  |
| DataTypes | number |  |

Initializes this BlockArea to an empty area of the specified size and origin of {0, 0, 0}. Any previous contents are lost.

### Overload 3: Create(Size)

| Name | Type | Notes |
| --- | --- | --- |
| Size | Vector3i |  |

Creates a new area of the specified size. Datatypes are set to baTypes + baMetas. Origin is set to all zeroes. BlockTypes are set to air, block metas to zero, blocklights to zero and skylights to full light.

### Overload 4: Create(Size, DataTypes)

| Name | Type | Notes |
| --- | --- | --- |
| Size | Vector3i |  |
| DataTypes | number |  |

Creates a new area of the specified size and contents. Origin is set to all zeroes. BlockTypes are set to air, block metas to zero, blocklights to zero and skylights to full light.

### Crop(AddMinX, SubMaxX, AddMinY, SubMaxY, AddMinZ, SubMaxZ)

| Name | Type | Notes |
| --- | --- | --- |
| AddMinX | number |  |
| SubMaxX | number |  |
| AddMinY | number |  |
| SubMaxY | number |  |
| AddMinZ | number |  |
| SubMaxZ | number |  |

Crops the specified number of blocks from each border. Modifies the size of this blockarea object.

### Overload 1: DoWithBlockEntityAt(BlockX, BlockY, BlockZ, Callback)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockY | number |  |
| BlockZ | number |  |
| Callback | function |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| HasCalled | boolean |  |

Calls the specified callback with the block entity at the specified absolute coords. The CallbackFunction has the following signature: <pre class="prettyprint lang-lua">function Callback({{cBlockEntity|BlockEntity}})</pre> Returns false if there's no block entity at the specified coords. Returns the value that the callback has returned otherwise.

### Overload 2: DoWithBlockEntityAt(Coords, Callback)

| Name | Type | Notes |
| --- | --- | --- |
| Coords | Vector3i |  |
| Callback | function |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| HasCalled | boolean |  |

Calls the specified callback with the block entity at the specified absolute coords. The CallbackFunction has the following signature: <pre class="prettyprint lang-lua">function Callback({{cBlockEntity|BlockEntity}})</pre> Returns false if there's no block entity at the specified coords. Returns the value that the callback has returned otherwise.

### Overload 1: DoWithBlockEntityRelAt(RelX, RelY, RelZ, Callback)

| Name | Type | Notes |
| --- | --- | --- |
| RelX | number |  |
| RelY | number |  |
| RelZ | number |  |
| Callback | function |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| HasCalled | boolean |  |

Calls the specified callback with the block entity at the specified relative coords. The CallbackFunction has the following signature: <pre class="prettyprint lang-lua">function Callback({{cBlockEntity|BlockEntity}})</pre> Returns false if there's no block entity at the specified coords. Returns the value that the callback has returned otherwise.

### Overload 2: DoWithBlockEntityRelAt(RelCoords, Callback)

| Name | Type | Notes |
| --- | --- | --- |
| RelCoords | Vector3i |  |
| Callback | function |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| HasCalled | boolean |  |

Calls the specified callback with the block entity at the specified relative coords. The CallbackFunction has the following signature: <pre class="prettyprint lang-lua">function Callback({{cBlockEntity|BlockEntity}})</pre> Returns false if there's no block entity at the specified coords. Returns the value that the callback has returned otherwise.

### DumpToRawFile(FileName)

| Name | Type | Notes |
| --- | --- | --- |
| FileName | string |  |

Dumps the raw data into a file. For debugging purposes only.

### Expand(SubMinX, AddMaxX, SubMinY, AddMaxY, SubMinZ, AddMaxZ)

| Name | Type | Notes |
| --- | --- | --- |
| SubMinX | number |  |
| AddMaxX | number |  |
| SubMinY | number |  |
| AddMaxY | number |  |
| SubMinZ | number |  |
| AddMaxZ | number |  |

Expands the specified number of blocks from each border. Modifies the size of this blockarea object. New blocks created with this operation are filled with zeroes.

### Fill(DataTypes, BlockType, BlockMeta, BlockLight, BlockSkyLight)

| Name | Type | Notes |
| --- | --- | --- |
| DataTypes | number |  |
| BlockType | number |  |
| BlockMeta (optional) | number |  |
| BlockLight (optional) | number |  |
| BlockSkyLight (optional) | number |  |

Fills the entire block area with the same values, specified. Uses the DataTypes param to determine which content types are modified.

### Overload 1: FillRelCuboid(RelCuboid, DataTypes, BlockType, BlockMeta, BlockLight, BlockSkyLight)

| Name | Type | Notes |
| --- | --- | --- |
| RelCuboid | cCuboid |  |
| DataTypes | number |  |
| BlockType | number |  |
| BlockMeta (optional) | number |  |
| BlockLight (optional) | number |  |
| BlockSkyLight (optional) | number |  |

Fills the specified cuboid (in relative coords) with the same values (like Fill() ).

### Overload 2: FillRelCuboid(MinRelX, MaxRelX, MinRelY, MaxRelY, MinRelZ, MaxRelZ, DataTypes, BlockType, BlockMeta, BlockLight, BlockSkyLight)

| Name | Type | Notes |
| --- | --- | --- |
| MinRelX | number |  |
| MaxRelX | number |  |
| MinRelY | number |  |
| MaxRelY | number |  |
| MinRelZ | number |  |
| MaxRelZ | number |  |
| DataTypes | number |  |
| BlockType | number |  |
| BlockMeta (optional) | number |  |
| BlockLight (optional) | number |  |
| BlockSkyLight (optional) | number |  |

Fills the specified cuboid with the same values (like Fill() ).

### ForEachBlockEntity(Coords, Callback)

| Name | Type | Notes |
| --- | --- | --- |
| Coords | Vector3i |  |
| Callback | function |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| HasProcessedAll | boolean |  |

Calls the specified callback with the block entity for each block entity contained in the object. Returns true if all block entities have been processed (including when there are zero block entities), or false if the callback has aborted the enumeration by returning true. The CallbackFunction has the following signature: <pre class="prettyprint lang-lua">function Callback({{cBlockEntity|BlockEntity}})</pre> The callback should return false or no value to continue with the next block entity, or true to abort the enumeration.

### GetBlockLight(BlockX, BlockY, BlockZ)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockY | number |  |
| BlockZ | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| BlockLight | number |  |

Returns the blocklight (emissive light) at the specified absolute coords

### GetBlockMeta(BlockX, BlockY, BlockZ)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockY | number |  |
| BlockZ | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| BlockMeta | number |  |

Returns the block meta at the specified absolute coords

### GetBlockSkyLight(BlockX, BlockY, BlockZ)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockY | number |  |
| BlockZ | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| BlockSkyLight | number |  |

Returns the skylight at the specified absolute coords

### GetBlockType(BlockX, BlockY, BlockZ)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockY | number |  |
| BlockZ | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| BLOCKTYPE | number |  |

Returns the block type at the specified absolute coords

### GetBlockTypeMeta(BlockX, BlockY, BlockZ)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockY | number |  |
| BlockZ | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| BlockType | number |  |
| BlockMeta | number |  |

Returns the block type and meta at the specified absolute coords

### GetBounds()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| Bounds | cCuboid |  |

Returns the {{cCuboid|cuboid}} that specifies the original coords of the world from which the area was read. Basically constructs a {{cCuboid}} out of GetOrigin() and GetOrigin() + GetCoordRange().

### GetCoordRange()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| MaxX | number |  |
| MaxY | number |  |
| MaxZ | number |  |

Returns the maximum relative coords in all 3 axes. See also GetSize().

### GetDataTypes()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the mask of datatypes (ba* constants added together) that the object is currently holding.

### GetNonAirCropRelCoords(IgnoredBlockType)

| Name | Type | Notes |
| --- | --- | --- |
| IgnoredBlockType (optional) | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| MinRelX | number |  |
| MinRelY | number |  |
| MinRelZ | number |  |
| MaxRelX | number |  |
| MaxRelY | number |  |
| MaxRelZ | number |  |

Returns the minimum and maximum coords in each direction for the first block in each direction of type different to IgnoredBlockType (E_BLOCK_AIR by default). If there are no non-ignored blocks within the area, or blocktypes are not present, the returned values are reverse-ranges (MinX <- m_RangeX, MaxX <- 0 etc.). IgnoreBlockType defaults to air.

### GetOrigin()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| OriginX | number |  |
| OriginY | number |  |
| OriginZ | number |  |

Returns the origin coords of where the area was read from.

### GetOriginX()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the origin x-coord

### GetOriginY()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the origin y-coord

### GetOriginZ()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the origin z-coord

### GetRelBlockLight(RelBlockX, RelBlockY, RelBlockZ)

| Name | Type | Notes |
| --- | --- | --- |
| RelBlockX | number |  |
| RelBlockY | number |  |
| RelBlockZ | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| NIBBLETYPE | number |  |

Returns the blocklight at the specified relative coords

### GetRelBlockMeta(RelBlockX, RelBlockY, RelBlockZ)

| Name | Type | Notes |
| --- | --- | --- |
| RelBlockX | number |  |
| RelBlockY | number |  |
| RelBlockZ | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| NIBBLETYPE | number |  |

Returns the block meta at the specified relative coords

### GetRelBlockSkyLight(RelBlockX, RelBlockY, RelBlockZ)

| Name | Type | Notes |
| --- | --- | --- |
| RelBlockX | number |  |
| RelBlockY | number |  |
| RelBlockZ | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| NIBBLETYPE | number |  |

Returns the skylight at the specified relative coords

### GetRelBlockType(RelBlockX, RelBlockY, RelBlockZ)

| Name | Type | Notes |
| --- | --- | --- |
| RelBlockX | number |  |
| RelBlockY | number |  |
| RelBlockZ | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| BLOCKTYPE | number |  |

Returns the block type at the specified relative coords

### GetRelBlockTypeMeta(RelBlockX, RelBlockY, RelBlockZ)

| Name | Type | Notes |
| --- | --- | --- |
| RelBlockX | number |  |
| RelBlockY | number |  |
| RelBlockZ | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| BLOCKTYPE | number |  |
| NIBBLETYPE | number |  |

Returns the block type and meta at the specified relative coords

### GetSize()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| SizeX | number |  |
| SizeY | number |  |
| SizeZ | number |  |

Returns the size of the area in all 3 axes. See also GetCoordRange().

### GetSizeX()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the size of the held data in the x-axis

### GetSizeY()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the size of the held data in the y-axis

### GetSizeZ()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the size of the held data in the z-axis

### GetVolume()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the volume of the area - the total number of blocks stored within.

### GetWEOffset()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | Vector3i |  |

Returns the WE offset, a data value sometimes stored in the schematic files. Cuberite doesn't use this value, but provides access to it using this method. The default is {0, 0, 0}.

### HasBlockEntities()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if current datatypes include block entities.

### HasBlockLights()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if current datatypes include blocklight

### HasBlockMetas()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if current datatypes include block metas

### HasBlockSkyLights()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if current datatypes include skylight

### HasBlockTypes()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if current datatypes include block types

### Overload 1: IsValidCoords(BlockX, BlockY, BlockZ)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockY | number |  |
| BlockZ | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if the specified absolute coords are within the area.

### Overload 2: IsValidCoords(Coords)

| Name | Type | Notes |
| --- | --- | --- |
| Coords | Vector3i |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if the specified absolute coords are within the area.

### **Static** IsValidDataTypeCombination(DataTypes)

| Name | Type | Notes |
| --- | --- | --- |
| DataTypes | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if the specified combination of datatypes (ba* constants added together) is valid. Most combinations are valid, but for example baBlockEntities without baTypes is an invalid combination.

### Overload 1: IsValidRelCoords(RelBlockX, RelBlockY, RelBlockZ)

| Name | Type | Notes |
| --- | --- | --- |
| RelBlockX | number |  |
| RelBlockY | number |  |
| RelBlockZ | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if the specified relative coords are within the area.

### Overload 2: IsValidRelCoords(RelCoords)

| Name | Type | Notes |
| --- | --- | --- |
| RelCoords | Vector3i |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if the specified relative coords are within the area.

### LoadFromSchematicFile(FileName)

| Name | Type | Notes |
| --- | --- | --- |
| FileName | string |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Clears current content and loads new content from the specified schematic file. Returns true if successful. Returns false and logs error if unsuccessful, old content is preserved in such a case.

### LoadFromSchematicString(SchematicData)

| Name | Type | Notes |
| --- | --- | --- |
| SchematicData | string |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Clears current content and loads new content from the specified string (assumed to contain .schematic data). Returns true if successful. Returns false and logs error if unsuccessful, old content is preserved in such a case.

### Overload 1: Merge(BlockAreaSrc, RelMinCoords, Strategy)

| Name | Type | Notes |
| --- | --- | --- |
| BlockAreaSrc | cBlockArea |  |
| RelMinCoords | number |  |
| Strategy | string |  |

Merges BlockAreaSrc into this object at the specified relative coords, using the specified strategy

### Overload 2: Merge(BlockAreaSrc, RelX, RelY, RelZ, Strategy)

| Name | Type | Notes |
| --- | --- | --- |
| BlockAreaSrc | cBlockArea |  |
| RelX | number |  |
| RelY | number |  |
| RelZ | number |  |
| Strategy | string |  |

Merges BlockAreaSrc into this object at the specified relative coords, using the specified strategy

### MirrorXY()

Mirrors this block area around the XY plane. Modifies blocks' metas (if present) to match (i. e. furnaces facing the opposite direction).

### MirrorXYNoMeta()

Mirrors this block area around the XY plane. Doesn't modify blocks' metas.

### MirrorXZ()

Mirrors this block area around the XZ plane. Modifies blocks' metas (if present)

### MirrorXZNoMeta()

Mirrors this block area around the XZ plane. Doesn't modify blocks' metas.

### MirrorYZ()

Mirrors this block area around the YZ plane. Modifies blocks' metas (if present)

### MirrorYZNoMeta()

Mirrors this block area around the YZ plane. Doesn't modify blocks' metas.

### Overload 1: Read(World, Cuboid)

| Name | Type | Notes |
| --- | --- | --- |
| World | cWorld |  |
| Cuboid | cCuboid |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| IsSuccess | boolean |  |

Reads the area from World, returns true if successful. baTypes and baMetas are read.

### Overload 2: Read(World, Cuboid, DataTypes)

| Name | Type | Notes |
| --- | --- | --- |
| World | cWorld |  |
| Cuboid | cCuboid |  |
| DataTypes | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| IsSuccess | boolean |  |

Reads the area from World, returns true if successful. DataTypes is the sum of baXXX datatypes to be read

### Overload 3: Read(World, Point1, Point2)

| Name | Type | Notes |
| --- | --- | --- |
| World | cWorld |  |
| Point1 | Vector3i |  |
| Point2 | Vector3i |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| IsSuccess | boolean |  |

Reads the area from World, returns true if successful. baTypes and baMetas are read.

### Overload 4: Read(World, Point1, Point2, DataTypes)

| Name | Type | Notes |
| --- | --- | --- |
| World | cWorld |  |
| Point1 | Vector3i |  |
| Point2 | Vector3i |  |
| DataTypes | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| IsSuccess | boolean |  |

Reads the area from World, returns true if successful. DataTypes is a sum of baXXX datatypes to be read.

### Overload 5: Read(World, MinX, MaxX, MinY, MaxY, MinZ, MaxZ)

| Name | Type | Notes |
| --- | --- | --- |
| World | cWorld |  |
| MinX | number |  |
| MaxX | number |  |
| MinY | number |  |
| MaxY | number |  |
| MinZ | number |  |
| MaxZ | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Reads the area from World, returns true if successful. baTypes and baMetas are read.

### Overload 6: Read(World, MinX, MaxX, MinY, MaxY, MinZ, MaxZ, DataTypes)

| Name | Type | Notes |
| --- | --- | --- |
| World | cWorld |  |
| MinX | number |  |
| MaxX | number |  |
| MinY | number |  |
| MaxY | number |  |
| MinZ | number |  |
| MaxZ | number |  |
| DataTypes | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Reads the area from World, returns true if successful. DataTypes is a sum of baXXX datatypes to read.

### Overload 1: RelLine(RelPoint1, RelPoint2, DataTypes, BlockType, BlockMeta, BlockLight, BlockSkyLight)

| Name | Type | Notes |
| --- | --- | --- |
| RelPoint1 | Vector3i |  |
| RelPoint2 | Vector3i |  |
| DataTypes | number |  |
| BlockType | number |  |
| BlockMeta (optional) | number |  |
| BlockLight (optional) | number |  |
| BlockSkyLight (optional) | number |  |

Draws a line between the two specified points. Sets only datatypes specified by DataTypes (baXXX constants).

### Overload 2: RelLine(RelX1, RelY1, RelZ1, RelX2, RelY2, RelZ2, DataTypes, BlockType, BlockMeta, BlockLight, BlockSkyLight)

| Name | Type | Notes |
| --- | --- | --- |
| RelX1 | number |  |
| RelY1 | number |  |
| RelZ1 | number |  |
| RelX2 | number |  |
| RelY2 | number |  |
| RelZ2 | number |  |
| DataTypes | number |  |
| BlockType | number |  |
| BlockMeta (optional) | number |  |
| BlockLight (optional) | number |  |
| BlockSkyLight (optional) | number |  |

Draws a line between the two specified points. Sets only datatypes specified by DataTypes (baXXX constants).

### RotateCCW()

Rotates the block area around the Y axis, counter-clockwise (east -> north). Modifies blocks' metas (if present) to match.

### RotateCCWNoMeta()

Rotates the block area around the Y axis, counter-clockwise (east -> north). Doesn't modify blocks' metas.

### RotateCW()

Rotates the block area around the Y axis, clockwise (north -> east). Modifies blocks' metas (if present) to match.

### RotateCWNoMeta()

Rotates the block area around the Y axis, clockwise (north -> east). Doesn't modify blocks' metas.

### SaveToSchematicFile(FileName)

| Name | Type | Notes |
| --- | --- | --- |
| FileName | string |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Saves the current contents to a schematic file. Returns true if successful.

### SaveToSchematicString()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | string |  |

Saves the current contents to a string (in a .schematic file format). Returns the data if successful, nil if failed.

### SetBlockLight(BlockX, BlockY, BlockZ, BlockLight)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockY | number |  |
| BlockZ | number |  |
| BlockLight | number |  |

Sets the blocklight at the specified absolute coords

### SetBlockMeta(BlockX, BlockY, BlockZ, BlockMeta)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockY | number |  |
| BlockZ | number |  |
| BlockMeta | number |  |

Sets the block meta at the specified absolute coords.

### SetBlockSkyLight(BlockX, BlockY, BlockZ, BlockSkyLight)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockY | number |  |
| BlockZ | number |  |
| BlockSkyLight | number |  |

Sets the skylight at the specified absolute coords

### SetBlockType(BlockX, BlockY, BlockZ, BlockType)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockY | number |  |
| BlockZ | number |  |
| BlockType | number |  |

Sets the block type at the specified absolute coords

### SetBlockTypeMeta(BlockX, BlockY, BlockZ, BlockType, BlockMeta)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockY | number |  |
| BlockZ | number |  |
| BlockType | number |  |
| BlockMeta | number |  |

Sets the block type and meta at the specified absolute coords

### Overload 1: SetOrigin(Origin)

| Name | Type | Notes |
| --- | --- | --- |
| Origin | Vector3i |  |

Resets the origin for the absolute coords. Only affects how absolute coords are translated into relative coords.

### Overload 2: SetOrigin(OriginX, OriginY, OriginZ)

| Name | Type | Notes |
| --- | --- | --- |
| OriginX | number |  |
| OriginY | number |  |
| OriginZ | number |  |

Resets the origin for the absolute coords. Only affects how absolute coords are translated into relative coords.

### SetRelBlockLight(RelBlockX, RelBlockY, RelBlockZ, BlockLight)

| Name | Type | Notes |
| --- | --- | --- |
| RelBlockX | number |  |
| RelBlockY | number |  |
| RelBlockZ | number |  |
| BlockLight | number |  |

Sets the blocklight at the specified relative coords

### SetRelBlockMeta(RelBlockX, RelBlockY, RelBlockZ, BlockMeta)

| Name | Type | Notes |
| --- | --- | --- |
| RelBlockX | number |  |
| RelBlockY | number |  |
| RelBlockZ | number |  |
| BlockMeta | number |  |

Sets the block meta at the specified relative coords

### SetRelBlockSkyLight(RelBlockX, RelBlockY, RelBlockZ, BlockSkyLight)

| Name | Type | Notes |
| --- | --- | --- |
| RelBlockX | number |  |
| RelBlockY | number |  |
| RelBlockZ | number |  |
| BlockSkyLight | number |  |

Sets the skylight at the specified relative coords

### SetRelBlockType(RelBlockX, RelBlockY, RelBlockZ, BlockType)

| Name | Type | Notes |
| --- | --- | --- |
| RelBlockX | number |  |
| RelBlockY | number |  |
| RelBlockZ | number |  |
| BlockType | number |  |

Sets the block type at the specified relative coords

### SetRelBlockTypeMeta(RelBlockX, RelBlockY, RelBlockZ, BlockType, BlockMeta)

| Name | Type | Notes |
| --- | --- | --- |
| RelBlockX | number |  |
| RelBlockY | number |  |
| RelBlockZ | number |  |
| BlockType | number |  |
| BlockMeta | number |  |

Sets the block type and meta at the specified relative coords

### Overload 1: SetWEOffset(Offset)

| Name | Type | Notes |
| --- | --- | --- |
| Offset | Vector3i |  |

Sets the WE offset, a data value sometimes stored in the schematic files. Mostly used for WorldEdit. Cuberite doesn't use this value, but provides access to it using this method.

### Overload 2: SetWEOffset(OffsetX, OffsetY, OffsetZ)

| Name | Type | Notes |
| --- | --- | --- |
| OffsetX | number |  |
| OffsetY | number |  |
| OffsetZ | number |  |

Sets the WE offset, a data value sometimes stored in the schematic files. Mostly used for WorldEdit. Cuberite doesn't use this value, but provides access to it using this method.

### Overload 1: Write(World, MinPoint)

| Name | Type | Notes |
| --- | --- | --- |
| World | cWorld |  |
| MinPoint | Vector3i |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| IsSuccess | boolean |  |

Writes the area into World at the specified coords, returns true if successful. All present data types are written.

### Overload 2: Write(World, MinPoint, DataTypes)

| Name | Type | Notes |
| --- | --- | --- |
| World | cWorld |  |
| MinPoint | Vector3i |  |
| DataTypes | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| IsSuccess | boolean |  |

Writes the area into World at the specified coords, returns true if successful. DataTypes is the sum of baXXX datatypes to write.

### Overload 3: Write(World, MinX, MinY, MinZ)

| Name | Type | Notes |
| --- | --- | --- |
| World | cWorld |  |
| MinX | number |  |
| MinY | number |  |
| MinZ | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| IsSuccess | boolean |  |

Writes the area into World at the specified coords, returns true if successful. All present data types are written.

### Overload 4: Write(World, MinX, MinY, MinZ, DataTypes)

| Name | Type | Notes |
| --- | --- | --- |
| World | cWorld |  |
| MinX | number |  |
| MinY | number |  |
| MinZ | number |  |
| DataTypes | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| IsSuccess | boolean |  |

Writes the area into World at the specified coords, returns true if successful. DataTypes is the sum of baXXX datatypes to write.

### constructor()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | cBlockArea |  |

Creates a new empty cBlockArea object

## Constants

| Name | Notes |
| --- | --- |
| baBlockEntities | Operations should work on block entities. Note that this flag is invalid without baTypes. |
| baLight | Operations should work on block (emissive) light |
| baMetas | Operations should work on block metas |
| baSkyLight | Operations should work on skylight |
| baTypes | Operation should work on block types |
| msDifference | Block becomes air if 'self' and src are the same. Otherwise it becomes the src block. |
| msFillAir | 'self' is overwritten by Src only where 'self' has air blocks |
| msImprint | Src overwrites 'self' anywhere where 'self' has non-air blocks |
| msLake | Special mode for merging lake images |
| msMask | The blocks that are exactly the same are kept in 'self', all differing blocks are replaced by air |
| msOverwrite | Src overwrites anything in 'self' |
| msSimpleCompare | The blocks that are exactly the same are replaced with air, all differing blocks are replaced by stone |
| msSpongePrint | Similar to msImprint, sponge block doesn't overwrite anything, all other blocks overwrite everything |

## Constant Groups


					The following constants are used to signalize the datatype to read or write:
				

### BATypes


					The Merge() function can use different strategies to combine the source and destination blocks.
					The following constants are used:
				

### eMergeStrategy

See below for a detailed explanation of the individual merge strategies.

## Additional Info

### Merge strategies

The strategy parameter specifies how individual blocks are combined together, using the table below.

| area block | | result | | |
| --- | --- | --- | --- | --- |
| this | Src | msOverwrite | msFillAir | msImprint |
| air | air | air | air | air |
| A | air | air | A | A |
| air | B | B | B | B |
| A | B | B | A | B |
| A | A | A | A | A |

So to sum up:

- msOverwrite completely overwrites all blocks with the Src's blocks

- msFillAir overwrites only those blocks that were air

- msImprint overwrites with only those blocks that are non-air

### Special strategies

For each strategy, evaluate the table rows from top downwards, the first match wins.

**msDifference** - changes all the blocks which are the same to air. Otherwise the source block gets placed.

area block | |  | Notes || * | B | B | The blocks are different so we use block B |
| B | B | Air | The blocks are the same so we get air. |

**msLake** - used for merging areas with lava and water lakes, in the appropriate generator.

| area block | |  | Notes |
| --- | --- | --- | --- |
| self | Src | result |  |
| A | sponge | A | Sponge is the NOP block |
| * | air | air | Air always gets hollowed out, even under the oceans |
| water | * | water | Water is never overwritten |
| lava | * | lava | Lava is never overwritten |
| * | water | water | Water always overwrites anything |
| * | lava | lava | Lava always overwrites anything |
| dirt | stone | stone | Stone overwrites dirt |
| grass | stone | stone | ... and grass |
| mycelium | stone | stone | ... and mycelium |
| A | stone | A | ... but nothing else |
| A | * | A | Everything else is left as it is |

**msSpongePrint** - used for most prefab-generators to merge the prefabs. Similar to
msImprint, but uses the sponge block as the NOP block instead, so that the prefabs may carve out air
pockets, too.

| area block | |  | Notes |
| --- | --- | --- | --- |
| self | Src | result |  |
| A | sponge | A | Sponge is the NOP block |
| * | B | B | Everything else overwrites anything |

**msMask** - the blocks that are the same in the other area are kept, all the
differing blocks are replaced with air. Meta is used in the comparison, too, two blocks of the
same type but different meta are considered different and thus replaced with air.

| area block | |  | Notes |
| --- | --- | --- | --- |
| self | Src | result |  |
| A | A | A | Same blocks are kept |
| A | non-A | air | Differing blocks are replaced with air |

**msDifference** - the blocks that are the same in both areas are replaced with air, all the
differing blocks are kept from the first area. Meta is used in the comparison, too, two blocks of the
same type but different meta are considered different.

| area block | |  | Notes |
| --- | --- | --- | --- |
| self | Src | result |  |
| A | A | air | Same blocks are replaced with air |
| A | non-A | A | Differing blocks are kept from 'self' |

**msSimpleCompare** - the blocks that are the same in both areas are replaced with air, all the
differing blocks are replaced with stone. Meta is used in the comparison, too, two blocks of the
same type but different meta are considered different.

| area block | |  | Notes |
| --- | --- | --- | --- |
| self | Src | result |  |
| A | A | air | Same blocks are replaced with air |
| A | non-A | stone | Differing blocks are replaced with stone |
