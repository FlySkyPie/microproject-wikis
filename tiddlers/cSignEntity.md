**Inherits from:** [cBlockEntity](#cBlockEntity)

A sign entity represents a sign in the world. This class is only used when generating chunks, so
that the plugins may generate signs within new chunks. See the code example in {{cChunkDesc}}.

## Functions

### GetLine(LineIndex)

| Name | Type | Notes |
| --- | --- | --- |
| LineIndex | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | string |  |

Returns the specified line. LineIndex is expected between 0 and 3. Returns empty string and logs to server console when LineIndex is invalid.

### SetLine(LineIndex, LineText)

| Name | Type | Notes |
| --- | --- | --- |
| LineIndex | number |  |
| LineText | string |  |

Sets the specified line. LineIndex is expected between 0 and 3. Logs to server console when LineIndex is invalid.

### SetLines(Line1, Line2, Line3, Line4)

| Name | Type | Notes |
| --- | --- | --- |
| Line1 | string |  |
| Line2 | string |  |
| Line3 | string |  |
| Line4 | string |  |

Sets all the sign's lines at once. Note that plugins should prefer to use {{cWorld}}:SetSignLines(), so that they can specify the player on whose behalf the sign is being set.
