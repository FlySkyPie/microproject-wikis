Manages the players' permissions. The players are assigned a single rank, which contains groups of
permissions and restrictions. The functions in this class query or modify these.

All the functions are static, call them using the `cRankManager:Function()` convention.

The players are identified by their UUID, to support player renaming.

The rank also contains specific "mesage visuals" - bits that are used for formatting messages from the
players. There's a message prefix, which is put in front of every message the player sends, and the
message suffix that is appended to each message. There's also a PlayerNameColorCode, which holds the
color that is used for the player's name in the messages.

Each rank can contain any number of permission groups. These groups allow for an easier setup of the
permissions - you can share groups among ranks, so the usual approach is to group similar permissions
together and add that group to any rank that should use those permissions.

Permissions are added to individual groups. Each group can support unlimited permissions. Note that
adding a permission to a group will make the permission available to all the ranks that contain that
permission group.

One rank is reserved as the Default rank. All players that don't have an explicit rank assigned to them
will behave as if assigned to this rank. The default rank can be changed to any other rank at any time.
Note that the default rank cannot be removed from the RankManager - RemoveRank() will change the default
rank to the replacement rank, if specified, and fail if no replacement rank is specified. Renaming the
default rank using RenameRank() will change the default rank to the new name.

## Functions

### **Static** AddGroup(GroupName)

| Name | Type | Notes |
| --- | --- | --- |
| GroupName | string |  |

Adds the group of the specified name. Logs a warning and does nothing if the group already exists.

### **Static** AddGroupToRank(GroupName, RankName)

| Name | Type | Notes |
| --- | --- | --- |
| GroupName | string |  |
| RankName | string |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Adds the specified group to the specified rank. Returns true on success, false on failure - if the group name or the rank name is not found.

### **Static** AddPermissionToGroup(Permission, GroupName)

| Name | Type | Notes |
| --- | --- | --- |
| Permission | string |  |
| GroupName | string |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Adds the specified permission to the specified group. Returns true on success, false on failure - if the group name is not found.

### **Static** AddRank(RankName, MsgPrefix, MsgSuffix, MsgNameColorCode)

| Name | Type | Notes |
| --- | --- | --- |
| RankName | string |  |
| MsgPrefix | string |  |
| MsgSuffix | string |  |
| MsgNameColorCode | string |  |

Adds a new rank of the specified name and with the specified message visuals. Logs an info message and does nothing if the rank already exists.

### **Static** AddRestrictionToGroup(Permission, GroupName)

| Name | Type | Notes |
| --- | --- | --- |
| Permission | string |  |
| GroupName | string |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Adds a new restriction to the specified group. Returns true if successful, false if it fails (no such group). No action if the group already has the restriction.

### **Static** ClearPlayerRanks()

Removes all player ranks from the database. Note that this doesn't change the cPlayer instances for the already connected players, you need to update all the instances manually.

### **Static** GetAllGroups()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | table |  |

Returns an array-table containing the names of all the groups that are known to the manager.

### **Static** GetAllPermissions()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | table |  |

Returns an array-table containing all the permissions that are known to the manager.

### **Static** GetAllPermissionsRestrictions()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | table |  |

Returns an array-table containing all the permissions and restrictions (intermixed together) that are known to the manager.

### **Static** GetAllPlayerUUIDs()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | table |  |

Returns the short uuids of all players stored in the rank DB, sorted by the players' names (case insensitive).

### **Static** GetAllRanks()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | table |  |

Returns an array-table containing the names of all the ranks that are known to the manager.

### **Static** GetAllRestrictions()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | table |  |

Returns an array-table containing all the restrictions that are known to the manager.

### **Static** GetDefaultRank()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | string |  |

Returns the name of the default rank. 

### **Static** GetGroupPermissions(GroupName)

| Name | Type | Notes |
| --- | --- | --- |
| GroupName | string |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | table |  |

Returns an array-table containing the permissions that the specified group contains.

### **Static** GetGroupRestrictions(GroupName)

| Name | Type | Notes |
| --- | --- | --- |
| GroupName | string |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | table |  |

Returns an array-table containing the restrictions that the specified group contains.

### **Static** GetPlayerGroups(PlayerUUID)

| Name | Type | Notes |
| --- | --- | --- |
| PlayerUUID | cUUID |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | table |  |

Returns an array-table of the names of the groups that are assigned to the specified player through their rank. Returns an empty table if the player is not known or has no rank or groups assigned to them.

### **Static** GetPlayerMsgVisuals(PlayerUUID)

| Name | Type | Notes |
| --- | --- | --- |
| PlayerUUID | cUUID |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| MsgPrefix | string |  |
| MsgSuffix | string |  |
| MsgNameColorCode | string |  |

Returns the message visuals assigned to the player. If the player is not explicitly assigned a rank, the default rank's visuals are returned. If there is an error, no value is returned at all.

### **Static** GetPlayerName(PlayerUUID)

| Name | Type | Notes |
| --- | --- | --- |
| PlayerUUID | cUUID |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| PlayerName | string |  |

Returns the last name that the specified player has, for a player in the ranks database. An empty string is returned if the player isn't in the database.

### **Static** GetPlayerPermissions(PlayerUUID)

| Name | Type | Notes |
| --- | --- | --- |
| PlayerUUID | cUUID |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | table |  |

Returns an array-table containing all permissions that the specified player is assigned through their rank. Returns the default rank's permissions if the player has no explicit rank assigned to them. Returns an empty array on error.

### **Static** GetPlayerRankName(PlayerUUID)

| Name | Type | Notes |
| --- | --- | --- |
| PlayerUUID | cUUID |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| RankName | string |  |

Returns the name of the rank that is assigned to the specified player. An empty string (NOT the default rank) is returned if the player has no rank assigned to them.

### **Static** GetRankGroups(RankName)

| Name | Type | Notes |
| --- | --- | --- |
| RankName | string |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | table |  |

Returns an array-table of the names of all the groups that are assigned to the specified rank. Returns an empty table if there is no such rank.

### **Static** GetRankPermissions(RankName)

| Name | Type | Notes |
| --- | --- | --- |
| RankName | string |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | table |  |

Returns an array-table of all the permissions that are assigned to the specified rank through its groups. Returns an empty table if there is no such rank.

### **Static** GetRankRestrictions(RankName)

| Name | Type | Notes |
| --- | --- | --- |
| RankName | string |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | table |  |

Returns an array-table of all the restrictions that are assigned to the specified rank through its groups. Returns an empty table if there is no such rank.

### **Static** GetRankVisuals(RankName)

| Name | Type | Notes |
| --- | --- | --- |
| RankName | string |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| MsgPrefix | string |  |
| MsgSuffix | string |  |
| MsgNameColorCode | string |  |

Returns the message visuals for the specified rank. Returns no value if the specified rank does not exist.

### **Static** GroupExists(GroupName)

| Name | Type | Notes |
| --- | --- | --- |
| GroupName | string |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true iff the specified group exists.

### **Static** IsGroupInRank(GroupName, RankName)

| Name | Type | Notes |
| --- | --- | --- |
| GroupName | string |  |
| RankName | string |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true iff the specified group is assigned to the specified rank.

### **Static** IsPermissionInGroup(Permission, GroupName)

| Name | Type | Notes |
| --- | --- | --- |
| Permission | string |  |
| GroupName | string |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true iff the specified permission is assigned to the specified group.

### **Static** IsPlayerRankSet(PlayerUUID)

| Name | Type | Notes |
| --- | --- | --- |
| PlayerUUID | cUUID |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true iff the specified player has a rank assigned to them.

### **Static** IsRestrictionInGroup(Restriction, GroupName)

| Name | Type | Notes |
| --- | --- | --- |
| Restriction | string |  |
| GroupName | string |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true iff the specified restriction is assigned to the specified group.

### **Static** RankExists(RankName)

| Name | Type | Notes |
| --- | --- | --- |
| RankName | string |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true iff the specified rank exists.

### **Static** RemoveGroup(GroupName)

| Name | Type | Notes |
| --- | --- | --- |
| GroupName | string |  |

Removes the specified group completely. The group will be removed from all the ranks using it and then erased from the manager. Logs an info message and does nothing if the group doesn't exist.

### **Static** RemoveGroupFromRank(GroupName, RankName)

| Name | Type | Notes |
| --- | --- | --- |
| GroupName | string |  |
| RankName | string |  |

Removes the specified group from the specified rank. The group will still exist, even if it isn't assigned to any rank. Logs an info message and does nothing if the group or rank doesn't exist.

### **Static** RemovePermissionFromGroup(Permission, GroupName)

| Name | Type | Notes |
| --- | --- | --- |
| Permission | string |  |
| GroupName | string |  |

Removes the specified permission from the specified group. Logs an info message and does nothing if the group doesn't exist.

### **Static** RemovePlayerRank(PlayerUUID)

| Name | Type | Notes |
| --- | --- | --- |
| PlayerUUID | cUUID |  |

Removes the player's rank; the player's left without a rank. Note that this doesn't change the {{cPlayer}} instances for the already connected players, you need to update all the instances manually. No action if the player has no rank assigned to them already.

### **Static** RemoveRank(RankName, ReplacementRankName)

| Name | Type | Notes |
| --- | --- | --- |
| RankName | string |  |
| ReplacementRankName (optional) | string |  |

Removes the specified rank. If ReplacementRankName is given, the players that have RankName will get their rank set to ReplacementRankName. If it isn't given, or is an invalid rank, the players will be removed from the manager, their ranks will be unset completely. Logs an info message and does nothing if the rank is not found.

### **Static** RemoveRestrictionFromGroup(Restriction, GroupName)

| Name | Type | Notes |
| --- | --- | --- |
| Restriction | string |  |
| GroupName | string |  |

Removes the specified restriction from the specified group.

### **Static** RenameGroup(OldName, NewName)

| Name | Type | Notes |
| --- | --- | --- |
| OldName | string |  |
| NewName | string |  |

Renames the specified group. Logs an info message and does nothing if the group is not found or the new name is already used.

### **Static** RenameRank(OldName, NewName)

| Name | Type | Notes |
| --- | --- | --- |
| OldName | string |  |
| NewName | string |  |

Renames the specified rank. Logs an info message and does nothing if the rank is not found or the new name is already used.

### **Static** SetDefaultRank(RankName)

| Name | Type | Notes |
| --- | --- | --- |
| RankName | string |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Sets the specified rank as the default rank. Returns true on success, false on failure (rank doesn't exist).

### **Static** SetPlayerRank(PlayerUUID, PlayerName, RankName)

| Name | Type | Notes |
| --- | --- | --- |
| PlayerUUID | cUUID |  |
| PlayerName | string |  |
| RankName | string |  |

Updates the rank for the specified player. The player name is provided for reference, the UUID is used for identification. Logs a warning and does nothing if the rank is not found.

### **Static** SetRankVisuals(RankName, MsgPrefix, MsgSuffix, MsgNameColorCode)

| Name | Type | Notes |
| --- | --- | --- |
| RankName | string |  |
| MsgPrefix | string |  |
| MsgSuffix | string |  |
| MsgNameColorCode | string |  |

Updates the rank's message visuals. Logs an info message and does nothing if rank not found.
