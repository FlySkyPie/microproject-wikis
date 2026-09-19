This class provides an easy-to-use interface for tracing lines through individual
blocks in the world. It can either be used to call the provided callbacks according
to what events it encounters along the way, or there are shortcut functions used for
the most popular tracing reasons - line of sight and solid hits.

## Functions

### Overload 1: **Static** FirstSolidHitTrace(World, StartX, StartY, StartZ, EndX, EndY, EndZ)

| Name | Type | Notes |
| --- | --- | --- |
| World | cWorld |  |
| StartX | number |  |
| StartY | number |  |
| StartZ | number |  |
| EndX | number |  |
| EndY | number |  |
| EndZ | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| HasHitSolid | boolean |  |
| HitCoords | Vector3d |  |
| HitBlockCoords | Vector3i |  |
| HitBlockFace | eBlockFace |  |

If the specified line hits a solid block, return true and the coordinates / face of the first such solid block hit. Returns false if there's no solid block on that line.

### Overload 2: **Static** FirstSolidHitTrace(World, Start, End)

| Name | Type | Notes |
| --- | --- | --- |
| World | cWorld |  |
| Start | Vector3d |  |
| End | Vector3d |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| HasHitSolid | boolean |  |
| HitCoords | Vector3d |  |
| HitBlockCoords | Vector3i |  |
| HitBlockFace | eBlockFace |  |

If the specified line hits a solid block, return true and the coordinates / face of the first such solid block hit. Returns false if there's no solid block on that line.

### Overload 1: **Static** LineOfSightTrace(World, StartX, StartY, StartZ, EndX, EndY, EndZ, Sight)

| Name | Type | Notes |
| --- | --- | --- |
| World | cWorld |  |
| StartX | number |  |
| StartY | number |  |
| StartZ | number |  |
| EndX | number |  |
| EndY | number |  |
| EndZ | number |  |
| Sight | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| CanSee | boolean |  |

Returns true if the two points specified are within line of sight of each other. The Sight parameter specifies which blocks are considered transparent for the trace, it is a combination of {{cLineBlockTracer#eLineOfSight|losXXX}} values added together.

### Overload 2: **Static** LineOfSightTrace(World, Start, End, Sight)

| Name | Type | Notes |
| --- | --- | --- |
| World | cWorld |  |
| Start | Vector3d |  |
| End | Vector3d |  |
| Sight | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| CanSee | boolean |  |

Returns true if the two points specified are within line of sight of each other. The Sight parameter specifies which blocks are considered transparent for the trace, it is a combination of {{cLineBlockTracer#eLineOfSight|losXXX}} values added together.

### Overload 1: **Static** Trace(World, Callbacks, StartX, StartY, StartZ, EndX, EndY, EndZ)

| Name | Type | Notes |
| --- | --- | --- |
| World | cWorld |  |
| Callbacks | table |  |
| StartX | number |  |
| StartY | number |  |
| StartZ | number |  |
| EndX | number |  |
| EndY | number |  |
| EndZ | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

(OBSOLETE, use the Vector3-based overload instead) Performs the trace on the specified line. Returns true if the entire trace was processed (no callback returned true)

### Overload 2: **Static** Trace(World, Callbacks, Start, End)

| Name | Type | Notes |
| --- | --- | --- |
| World | cWorld |  |
| Callbacks | table |  |
| Start | Vector3d |  |
| End | Vector3d |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Performs the trace on the specified line. Returns true if the entire trace was processed (no callback returned true)

## Constants

| Name | Notes |
| --- | --- |
| losAir | LineOfSight tracing can 'see' through air blocks. |
| losLava | LineOfSight tracing can 'see' through lava blocks. |
| losWater | LineOfSight tracing can 'see' through water blocks. |

## Constant Groups

The following constants are used to speficy which blocks are see-through when tracing a LineOfSight trace. Add them together to make up the Sight parameter.

### eLineOfSight

## Additional Info

### Callbacks

The Callbacks in the Trace() function is a table that contains named functions. Cuberite will call
individual functions from that table for the events that occur on the line - hitting a block, going out of
valid world data etc. The following table lists all the available callbacks. If the callback function is
not defined, Cuberite skips it. Each function can return a bool value, if it returns true, the tracing is
aborted and Trace() returns false.
Note: The folowing can only be used when using the Vector3-based Trace() function. When using
the number-based overload, the callbacks receive number-based coordinates (see Deprecated
Callbacks below).

| Name | Parameters | Notes |
| --- | --- | --- |
| OnNextBlock | BlockPos, BlockType, BlockMeta, EntryFace | Called when the ray hits a new valid block. The block type and meta is given. EntryFace is one of the BLOCK\_FACE\_ constants indicating which "side" of the block got hit by the ray. |
| OnNextBlockNoData | BlockPos, EntryFace | Called when the ray hits a new block, but the block is in an unloaded chunk - no valid data is available. Only the coords and the entry face are given. |
| OnOutOfWorld | BlockPos | Called when the ray goes outside of the world (Y-wise); the coords specify the exact exit point. Note that for other paths than lines (considered for future implementations) the path may leave the world and go back in again later, in such a case this callback is followed by OnIntoWorld() and further OnNextBlock() calls. |
| OnIntoWorld | BlockPos | Called when the ray enters the world (Y-wise); the coords specify the exact entry point. |
| OnNoMoreHits |  | Called when the path is sure not to hit any more blocks. This is the final callback, no more callbacks are called after this function. Unlike the other callbacks, this function doesn't have a return value. |
| OnNoChunk |  | Called when the ray enters a chunk that is not loaded. This usually means that the tracing is aborted. Unlike the other callbacks, this function doesn't have a return value. |

### Deprecated Callbacks

When using the deprecated number-based Trace function, Cuberite will instead assume the following signatures for the callbacks:

| Name | Parameters | Notes |
| --- | --- | --- |
| OnNextBlock | BlockX, BlockY, BlockZ, BlockType, BlockMeta, EntryFace | Called when the ray hits a new valid block. The block type and meta is given. EntryFace is one of the BLOCK\_FACE\_ constants indicating which "side" of the block got hit by the ray. |
| OnNextBlockNoData | BlockX, BlockY, BlockZ, EntryFace | Called when the ray hits a new block, but the block is in an unloaded chunk - no valid data is available. Only the coords and the entry face are given. |
| OnOutOfWorld | X, Y, Z | Called when the ray goes outside of the world (Y-wise); the coords specify the exact exit point. Note that for other paths than lines (considered for future implementations) the path may leave the world and go back in again later, in such a case this callback is followed by OnIntoWorld() and further OnNextBlock() calls. |
| OnIntoWorld | X, Y, Z | Called when the ray enters the world (Y-wise); the coords specify the exact entry point. |

### Example

The following example is taken from the Debuggers plugin. It is a command handler function for the
"/spidey" command that creates a line of cobweb blocks from the player's eyes up to 50 blocks away in
the direction they're looking, but only through the air.

```
function HandleSpideyCmd(a_Split, a_Player)
	local World = a_Player:GetWorld();

	local Callbacks = {
		OnNextBlock = function(a_BlockPos, a_BlockType, a_BlockMeta)
			if (a_BlockType ~= E_BLOCK_AIR) then
				-- abort the trace
				return true;
			end
			World:SetBlock(a_BlockPos, E_BLOCK_COBWEB, 0);
		end
	};

	local EyePos = a_Player:GetEyePosition();
	local LookVector = a_Player:GetLookVector();
	LookVector:Normalize();  -- Make the vector 1 m long

	-- Start cca 2 blocks away from the eyes
	local Start = EyePos + LookVector + LookVector;
	local End = EyePos + LookVector * 50;

	cLineBlockTracer.Trace(World, Callbacks, Start, End);

	return true;
end
```
