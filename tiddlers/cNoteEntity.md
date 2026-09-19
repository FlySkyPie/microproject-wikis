**Inherits from:** [cBlockEntity](#cBlockEntity)

This class represents a note block entity in the world. It takes care of the note block's note,
and also can play the sound, either when the {{cPlayer|player}} right-clicks it, redstone activates
it, or upon a plugin's request.

The note is stored as an integer between 0 and 24.

## Functions

### GetNote()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the current note set for the block

### GetPitch()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

(<b>DEPRECATED</b>) Please use cNoteEntity:GetNote. Returns the current pitch set for the block

### IncrementNote()

Adds 1 to the current note. Wraps around to 0 when the note cannot go any higher.

### IncrementPitch()

(<b>DEPRECATED</b>) Please use cNoteEntity:IncrementNote. Adds 1 to the current pitch. Wraps around to 0 when the pitch cannot go any higher.

### SetNote(Note)

| Name | Type | Notes |
| --- | --- | --- |
| Note | number |  |

Sets a new note for the block.

### SetPitch(Pitch)

| Name | Type | Notes |
| --- | --- | --- |
| Pitch | number |  |

(<b>DEPRECATED</b>) Please use cNoteEntity:SetNote. Sets a new note for the block.
