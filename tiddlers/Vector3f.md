A Vector3f object uses floating point values to describe a point in space.

See also {{Vector3d}} for double-precision floating point 3D coords and {{Vector3i}} for integer
3D coords.

## Functions

### Abs()

Updates each coord to its absolute value.

### Ceil()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | Vector3i |  |

Returns a new {{Vector3i}} object with coords set to math.ceil of this vector's coords.

### Clamp(min, max)

| Name | Type | Notes |
| --- | --- | --- |
| min | number |  |
| max | number |  |

Clamps each coord into the specified range.

### Cross(Other)

| Name | Type | Notes |
| --- | --- | --- |
| Other | Vector3f |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | Vector3f |  |

Returns a new Vector3f object that holds the cross product of this vector and the specified vector.

### Dot(Other)

| Name | Type | Notes |
| --- | --- | --- |
| Other | Vector3f |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the dot product of this vector and the specified vector.

### Equals(Other)

| Name | Type | Notes |
| --- | --- | --- |
| Other | Vector3f |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if the specified vector is exactly equal to this vector. Note that this is subject to (possibly imprecise) floating point math.

### EqualsEps(Other, Eps)

| Name | Type | Notes |
| --- | --- | --- |
| Other | Vector3f |  |
| Eps | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if the differences between each corresponding coords of this vector and the one specified, are less than the specified Eps.

### Floor()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | Vector3i |  |

Returns a new {{Vector3i}} object with coords set to math.floor of this vector's coords.

### HasNonZeroLength()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if the vector has at least one coord non-zero. Note that this is subject to (possibly imprecise) floating point math.

### Length()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the (euclidean) length of this vector

### LineCoeffToXYPlane(Vector3f, Z)

| Name | Type | Notes |
| --- | --- | --- |
| Vector3f | Vector3f |  |
| Z | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the coefficient for the line from the specified vector through this vector to reach the specified Z coord. The result satisfies the following equation: (this + Result * (Param - this)).z = Z. Returns the NO_INTERSECTION constant if there's no intersection.

### LineCoeffToXZPlane(Vector3f, Y)

| Name | Type | Notes |
| --- | --- | --- |
| Vector3f | Vector3f |  |
| Y | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the coefficient for the line from the specified vector through this vector to reach the specified Y coord. The result satisfies the following equation: (this + Result * (Param - this)).y = Y. Returns the NO_INTERSECTION constant if there's no intersection.

### LineCoeffToYZPlane(Vector3f, X)

| Name | Type | Notes |
| --- | --- | --- |
| Vector3f | Vector3f |  |
| X | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the coefficient for the line from the specified vector through this vector to reach the specified X coord. The result satisfies the following equation: (this + Result * (Param - this)).x = X. Returns the NO_INTERSECTION constant if there's no intersection.

### Overload 1: Move(X, Y, Z)

| Name | Type | Notes |
| --- | --- | --- |
| X | number |  |
| Y | number |  |
| Z | number |  |

Adds the specified offsets to each coord, effectively moving the vector by the specified coord offsets.

### Overload 2: Move(Diff)

| Name | Type | Notes |
| --- | --- | --- |
| Diff | Vector3f |  |

Adds the specified vector to this vector. Is slightly better performant than adding with a "+" because this doesn't create a new object for the result.

### Normalize()

Normalizes this vector (makes it 1 unit long while keeping the direction). FIXME: Fails for zero vectors.

### NormalizeCopy()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | Vector3f |  |

Returns a copy of this vector that is normalized (1 unit long while keeping the same direction). FIXME: Fails for zero vectors.

### Set(x, y, z)

| Name | Type | Notes |
| --- | --- | --- |
| x | number |  |
| y | number |  |
| z | number |  |

Sets all the coords of the vector at once.

### SqrLength()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the (euclidean) length of this vector, squared. This operation is slightly less computationally expensive than Length(), while it conserves some properties of Length(), such as comparison.

### TurnCCW()

Rotates the vector 90 degrees counterclockwise around the vertical axis. Note that this is specific to minecraft's axis ordering, which is X+ left, Z+ down.

### TurnCW()

Rotates the vector 90 degrees clockwise around the vertical axis. Note that this is specific to minecraft's axis ordering, which is X+ left, Z+ down.

### addedX(ofs)

| Name | Type | Notes |
| --- | --- | --- |
| ofs | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | Vector3f |  |

Returns a copy of the vector, moved by the specified offset on the X axis

### addedXZ(ofsX, ofsZ)

| Name | Type | Notes |
| --- | --- | --- |
| ofsX | number |  |
| ofsZ | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | Vector3f |  |

Returns a copy of the vector, moved by the specified offsets on the X and Z axes

### addedY(ofs)

| Name | Type | Notes |
| --- | --- | --- |
| ofs | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | Vector3f |  |

Returns a copy of the vector, moved by the specified offset on the Y axis

### addedZ(ofs)

| Name | Type | Notes |
| --- | --- | --- |
| ofs | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | Vector3f |  |

Returns a copy of the vector, moved by the specified offset on the Z axis

### Overload 1: constructor()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | Vector3f |  |

Creates a new Vector3f object with zero coords

### Overload 2: constructor(x, y, z)

| Name | Type | Notes |
| --- | --- | --- |
| x | number |  |
| y | number |  |
| z | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | Vector3f |  |

Creates a new Vector3f object with the specified coords

### Overload 3: constructor(Vector3f)

| Name | Type | Notes |
| --- | --- | --- |
| Vector3f | Vector3f |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | Vector3f |  |

Creates a new Vector3f object as a copy of the specified vector

### Overload 4: constructor(Vector3d)

| Name | Type | Notes |
| --- | --- | --- |
| Vector3d | Vector3d |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | Vector3f |  |

Creates a new Vector3f object as a copy of the specified {{Vector3d}}

### Overload 5: constructor(Vector3i)

| Name | Type | Notes |
| --- | --- | --- |
| Vector3i | Vector3i |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | Vector3f |  |

Creates a new Vector3f object as a copy of the specified {{Vector3i}}

### Overload 1: operator_div(PerCoordDivisor)

| Name | Type | Notes |
| --- | --- | --- |
| PerCoordDivisor | Vector3f |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | Vector3f |  |

Returns a new Vector3f object with each coord divided by the corresponding coord from the given vector.

### Overload 2: operator_div(Divisor)

| Name | Type | Notes |
| --- | --- | --- |
| Divisor | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | Vector3f |  |

Returns a new Vector3f object with each coord divided by the specified number.

### Overload 1: operator_mul(PerCoordMultiplier)

| Name | Type | Notes |
| --- | --- | --- |
| PerCoordMultiplier | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | Vector3f |  |

Returns a new Vector3f object that has each of its coords multiplied by the specified number

### Overload 2: operator_mul(Multiplier)

| Name | Type | Notes |
| --- | --- | --- |
| Multiplier | Vector3f |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | Vector3f |  |

Returns a new Vector3f object that has each of its coords multiplied by the respective coord of the specified vector.

### operator_plus(Other)

| Name | Type | Notes |
| --- | --- | --- |
| Other | Vector3f |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | Vector3f |  |

Returns a new Vector3f object that holds the vector sum of this vector and the specified vector.

### Overload 1: operator_sub(Subtrahend)

| Name | Type | Notes |
| --- | --- | --- |
| Subtrahend | Vector3f |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | Vector3f |  |

Returns a new Vector3f object that holds the vector differrence between this vector and the specified vector.

### Overload 2: operator_sub()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | Vector3f |  |

Returns a new Vector3f that is a negative of this vector (all coords multiplied by -1).

## Constants

| Name | Notes |
| --- | --- |
| EPS | The max difference between two coords for which the coords are assumed equal (in LineCoeffToXYPlane() et al). |
| NO_INTERSECTION | Special return value for the LineCoeffToXYPlane() et al meaning that there's no intersection with the plane. |

## Variables

| Name | Type | Notes |
| --- | --- | --- |
| x | number | The X coord of the vector. |
| y | number | The Y coord of the vector. |
| z | number | The Z coord of the vector. |
