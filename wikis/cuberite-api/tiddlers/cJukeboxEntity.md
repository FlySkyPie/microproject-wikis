**Inherits from:** [cBlockEntity](#cBlockEntity)

This class represents a jukebox in the world. It can play the records, either when the
{{cPlayer|player}} uses the record on the jukebox, or when a plugin instructs it to play.

## Functions

### EjectRecord()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Ejects the current record as a {{cPickup|pickup}}. No action if there's no current record. To remove record without generating the pickup, use SetRecord(0). Returns true if pickup ejected.

### GetRecord()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the record currently present. Zero for no record, E_ITEM_*_DISC for records.

### IsPlayingRecord()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if the jukebox is playing a record.

### **Static** IsRecordItem(ItemType)

| Name | Type | Notes |
| --- | --- | --- |
| ItemType | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if the specified item is a record that can be played.

### PlayRecord(RecordItemType)

| Name | Type | Notes |
| --- | --- | --- |
| RecordItemType | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Plays the specified Record. Return false if the parameter isn't a playable Record (E_ITEM_XXX_DISC). If there is a record already playing, ejects it first.

### SetRecord(RecordItemType)

| Name | Type | Notes |
| --- | --- | --- |
| RecordItemType | number |  |

Sets the currently present record. Use zero for no record, or E_ITEM_*_DISC for records.
