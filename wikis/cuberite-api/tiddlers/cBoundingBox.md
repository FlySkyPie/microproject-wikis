Represents two sets of coordinates, minimum and maximum for each direction; thus defining an
axis-aligned cuboid with floating-point boundaries. It supports operations changing the size and
position of the box, as well as querying whether a point or another BoundingBox is inside the box.

All the points within the coordinate limits (inclusive the edges) are considered "inside" the box.
However, for intersection purposes, if the intersection is "sharp" in any coord (min1 == max2, i. e.
zero volume), the boxes are considered non-intersecting.

## Functions

### Overload 1: CalcLineIntersection(LineStart, LinePt2)

| Name | Type | Notes |
| --- | --- | --- |
| LineStart | Vector3d |  |
| LinePt2 | Vector3d |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| DoesIntersect | boolean |  |
| LineCoeff | number |  |
| Face | eBlockFace |  |

Calculates the intersection of a ray (half-line), given by two of its points, with the bounding box. Returns false if the line doesn't intersect the bounding box, or true, together with coefficient of the intersection (how much of the difference between the two ray points is needed to reach the intersection), and the face of the box which is intersected.

### Overload 2: **Static** CalcLineIntersection(BoxMin, BoxMax, LineStart, LinePt2)

| Name | Type | Notes |
| --- | --- | --- |
| BoxMin | Vector3d |  |
| BoxMax | Vector3d |  |
| LineStart | Vector3d |  |
| LinePt2 | Vector3d |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| DoesIntersect | boolean |  |
| LineCoeff | number |  |
| Face | eBlockFace |  |

Calculates the intersection of a ray (half-line), given by two of its points, with the bounding box specified as its minimum and maximum coords. Returns false if the line doesn't intersect the bounding box, or true, together with coefficient of the intersection (how much of the difference between the two ray points is needed to reach the intersection), and the face of the box which is intersected.

### DoesIntersect(OtherBoundingBox)

| Name | Type | Notes |
| --- | --- | --- |
| OtherBoundingBox | cBoundingBox |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if the two bounding boxes have an intersection of nonzero volume.

### Expand(ExpandX, ExpandY, ExpandZ)

| Name | Type | Notes |
| --- | --- | --- |
| ExpandX | number |  |
| ExpandY | number |  |
| ExpandZ | number |  |

Expands this bounding box by the specified amount in each direction (so the box becomes larger by 2 * Expand in each axis).

### GetMax()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| Point | Vector3d |  |

Returns the boundary point with the maximum coords

### GetMaxX()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the maximum X coord of the bounding box

### GetMaxY()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the maximum Y coord of the bounding box

### GetMaxZ()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the maximum Z coord of the bounding box

### GetMin()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| Point | Vector3d |  |

Returns the boundary point with the minimum coords

### GetMinX()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the minimum X coord of the bounding box

### GetMinY()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the minimum Y coord of the bounding box

### GetMinZ()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the minimum Z coord of the bounding box

### Intersect(OtherBbox)

| Name | Type | Notes |
| --- | --- | --- |
| OtherBbox | cBoundingBox |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |
| Intersection | cBoundingBox |  |

Checks if the intersection between this bounding box and another one is non-empty. Returns false if the intersection is empty, true and a new cBoundingBox representing the intersection of the two boxes.

### Overload 1: IsInside(Point)

| Name | Type | Notes |
| --- | --- | --- |
| Point | Vector3d |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if the specified point is inside (including on the edge) of the box.

### Overload 2: IsInside(PointX, PointY, PointZ)

| Name | Type | Notes |
| --- | --- | --- |
| PointX | number |  |
| PointY | number |  |
| PointZ | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if the specified point is inside (including on the edge) of the box.

### Overload 3: IsInside(OtherBoundingBox)

| Name | Type | Notes |
| --- | --- | --- |
| OtherBoundingBox | cBoundingBox |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if OtherBoundingBox is inside of this box.

### Overload 4: IsInside(OtherBoxMin, OtherBoxMax)

| Name | Type | Notes |
| --- | --- | --- |
| OtherBoxMin | Vector3d |  |
| OtherBoxMax | Vector3d |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if the other bounding box, specified by its 2 corners, is inside of this box.

### Overload 5: **Static** IsInside(Min, Max, Point)

| Name | Type | Notes |
| --- | --- | --- |
| Min | Vector3d |  |
| Max | Vector3d |  |
| Point | Vector3d |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if the specified point is inside the bounding box specified by its min / max corners

### Overload 6: **Static** IsInside(Min, Max, X, Y, Z)

| Name | Type | Notes |
| --- | --- | --- |
| Min | Vector3d |  |
| Max | Vector3d |  |
| X | number |  |
| Y | number |  |
| Z | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if the specified point is inside the bounding box specified by its min / max corners

### Overload 1: Move(OffsetX, OffsetY, OffsetZ)

| Name | Type | Notes |
| --- | --- | --- |
| OffsetX | number |  |
| OffsetY | number |  |
| OffsetZ | number |  |

Moves the bounding box by the specified offset in each axis

### Overload 2: Move(Offset)

| Name | Type | Notes |
| --- | --- | --- |
| Offset | Vector3d |  |

Moves the bounding box by the specified offset in each axis

### Union(OtherBoundingBox)

| Name | Type | Notes |
| --- | --- | --- |
| OtherBoundingBox | cBoundingBox |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | cBoundingBox |  |

Returns the smallest bounding box that contains both OtherBoundingBox and this bounding box. Note that unlike the strict geometrical meaning of "union", this operation actually returns a cBoundingBox.

### Overload 1: constructor(MinX, MaxX, MinY, MaxY, MinZ, MaxZ)

| Name | Type | Notes |
| --- | --- | --- |
| MinX | number |  |
| MaxX | number |  |
| MinY | number |  |
| MaxY | number |  |
| MinZ | number |  |
| MaxZ | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | cBoundingBox |  |

Creates a new bounding box with the specified edges

### Overload 2: constructor(Min, Max)

| Name | Type | Notes |
| --- | --- | --- |
| Min | Vector3d |  |
| Max | Vector3d |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | cBoundingBox |  |

Creates a new bounding box with the coords specified as two vectors

### Overload 3: constructor(Pos, Radius, Height)

| Name | Type | Notes |
| --- | --- | --- |
| Pos | Vector3d |  |
| Radius | number |  |
| Height | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | cBoundingBox |  |

Creates a new bounding box from the position given and radius (X/Z) and height. Radius is added from X/Z to calculate the maximum coords and subtracted from X/Z to get the minimum; minimum Y is set to Pos.y and maxumim Y to Pos.y plus Height. This corresponds with how {{cEntity|entities}} are represented in Minecraft.

### Overload 4: constructor(OtherBoundingBox)

| Name | Type | Notes |
| --- | --- | --- |
| OtherBoundingBox | cBoundingBox |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | cBoundingBox |  |

Creates a new copy of the given bounding box. Same result can be achieved by using a simple assignment.

### Overload 5: constructor(Pos, CubeSideLength)

| Name | Type | Notes |
| --- | --- | --- |
| Pos | Vector3d |  |
| CubeSideLength | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | cBoundingBox |  |

Creates a new bounding box as a cube with the specified side length centered around the specified point.
