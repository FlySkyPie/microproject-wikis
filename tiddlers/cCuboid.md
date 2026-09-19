cCuboid offers some native support for integral-boundary cuboids. A cuboid internally consists of
two {{Vector3i}}-s. By default the cuboid doesn't make any assumptions about the defining points,
but for most of the operations in the cCuboid class, the p1 member variable is expected to be the
minima and the p2 variable the maxima. The Sort() function guarantees this condition.

The Cuboid considers both its edges inclusive.

## Functions

### Overload 1: Assign(SrcCuboid)

| Name | Type | Notes |
| --- | --- | --- |
| SrcCuboid | cCuboid |  |

Copies all the coords from the src cuboid to this cuboid. Sort-state is ignored.

### Overload 2: Assign(Point1, Point2)

| Name | Type | Notes |
| --- | --- | --- |
| Point1 | Vector3i |  |
| Point2 | Vector3i |  |

Assigns all the coords to the specified values. Sort-state is ignored.

### Clamp(Limits)

| Name | Type | Notes |
| --- | --- | --- |
| Limits | cCuboid |  |

Clamps this cuboid, so that it doesn't reach outside of Limits in any direction. Assumes both cuboids are sorted.

### ClampSize(MaxSize)

| Name | Type | Notes |
| --- | --- | --- |
| MaxSize | Vector3i |  |

Clamps this cuboid's p2 so that the cuboid's size doesn't exceed the specified max size. Assumes the cuboid is sorted.

### ClampX(MinX, MaxX)

| Name | Type | Notes |
| --- | --- | --- |
| MinX | number |  |
| MaxX | number |  |

Clamps both X coords into the range provided. Sortedness-agnostic.

### ClampY(MinY, MaxY)

| Name | Type | Notes |
| --- | --- | --- |
| MinY | number |  |
| MaxY | number |  |

Clamps both Y coords into the range provided. Sortedness-agnostic.

### ClampZ(MinZ, MaxZ)

| Name | Type | Notes |
| --- | --- | --- |
| MinZ | number |  |
| MaxZ | number |  |

Clamps both Z coords into the range provided. Sortedness-agnostic.

### DifX()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the difference between the two X coords (X-size minus 1). Assumes sorted.

### DifY()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the difference between the two Y coords (Y-size minus 1). Assumes sorted.

### DifZ()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the difference between the two Z coords (Z-size minus 1). Assumes sorted.

### DoesIntersect(OtherCuboid)

| Name | Type | Notes |
| --- | --- | --- |
| OtherCuboid | cCuboid |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if this cuboid has at least one voxel in common with OtherCuboid. Note that edges are considered inclusive. Assumes both sorted.

### Engulf(Point)

| Name | Type | Notes |
| --- | --- | --- |
| Point | Vector3i |  |

If needed, expands the cuboid to include the specified point. Doesn't shrink. Assumes sorted. 

### Expand(SubMinX, AddMaxX, SubMinY, AddMaxY, SubMinZ, AddMaxZ)

| Name | Type | Notes |
| --- | --- | --- |
| SubMinX | number |  |
| AddMaxX | number |  |
| SubMinY | number |  |
| AddMaxY | number |  |
| SubMinZ | number |  |
| AddMaxZ | number |  |

Expands the cuboid by the specified amount in each direction. Works on unsorted cuboids as well. NOTE: this function doesn't check for underflows.

### GetVolume()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the volume of the cuboid, in blocks. Note that the volume considers both coords inclusive. Works on unsorted cuboids, too.

### IsCompletelyInside(OuterCuboid)

| Name | Type | Notes |
| --- | --- | --- |
| OuterCuboid | cCuboid |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if this cuboid is completely inside (in all directions) in OuterCuboid. Assumes both sorted.

### Overload 1: IsInside(Point)

| Name | Type | Notes |
| --- | --- | --- |
| Point | Vector3i |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if the specified point (integral coords) is inside this cuboid. Assumes sorted.

### Overload 2: IsInside(Point)

| Name | Type | Notes |
| --- | --- | --- |
| Point | Vector3d |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if the specified point (floating-point coords) is inside this cuboid. Assumes sorted.

### IsSorted()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if this cuboid is sorted

### Move(Offset)

| Name | Type | Notes |
| --- | --- | --- |
| Offset | Vector3i |  |

Adds the specified offsets to each respective coord, effectively moving the Cuboid. Sort-state is ignored and preserved.

### Sort()

Sorts the internal representation so that p1 contains the lesser coords and p2 contains the greater coords.

### Overload 1: constructor()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | cCuboid |  |

Creates a new Cuboid object with all-zero coords

### Overload 2: constructor(OtherCuboid)

| Name | Type | Notes |
| --- | --- | --- |
| OtherCuboid | cCuboid |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | cCuboid |  |

Creates a new Cuboid object as a copy of OtherCuboid

### Overload 3: constructor(Point1, Point2)

| Name | Type | Notes |
| --- | --- | --- |
| Point1 | Vector3i |  |
| Point2 | Vector3i |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | cCuboid |  |

Creates a new Cuboid object with the specified points as its corners.

### Overload 4: constructor(X, Y, Z)

| Name | Type | Notes |
| --- | --- | --- |
| X | number |  |
| Y | number |  |
| Z | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | cCuboid |  |

Creates a new Cuboid object with the specified point as both its corners (the cuboid has a size of 1 in each direction).

## Variables

| Name | Type | Notes |
| --- | --- | --- |
| p1 | [Vector3i](#Vector3i) | The first corner. Usually the lesser of the two coords in each set |
| p2 | [Vector3i](#Vector3i) | The second corner. Usually the larger of the two coords in each set |
