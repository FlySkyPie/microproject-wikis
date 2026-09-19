cWorld is the game world. It is the hub of all the information managed by individual classes,
providing convenient access to them. Cuberite supports multiple worlds in any combination of
world types. You can have two overworlds, three nethers etc. To enumerate all world the server
provides, use the {{cRoot}}:ForEachWorld() function.

The world data is held in individual chunks. Each chunk consists of 16 (x) * 16 (z) * 256 (y)
blocks, each block is specified by its block type (8-bit) and block metadata (4-bit).
Additionally, each block has two light values calculated - skylight (how much daylight it receives)
and blocklight (how much light from light-emissive blocks it receives), both 4-bit.

Each world runs several separate threads used for various housekeeping purposes, the most important
of those is the Tick thread. This thread updates the game logic 20 times per second, and it is
the thread where all the gameplay actions are evaluated. Liquid physics, entity interactions,
player movement etc., all are applied in this thread.

Additional threads include the generation thread (generates new chunks as needed, storage thread
(saves and loads chunk from the disk), lighting thread (updates block light values) and the
chunksender thread (compresses chunks to send to the clients).

The world provides access to all its {{cPlayer|players}}, {{cEntity|entities}} and {{cBlockEntity|block
entities}}. Because of multithreading issues, individual objects cannot be retrieved for indefinite
handling, but rather must be modified in callbacks, within which they are guaranteed to stay valid.

Physics for individual blocks are handled by the simulators. These will fire in each tick for all
blocks that have been scheduled for simulator update ("simulator wakeup"). The simulators include
liquid physics, falling blocks, fire spreading and extinguishing and redstone.

Game time is also handled by the world. It provides the time-of-day and the total world age.

## Functions

### AreCommandBlocksEnabled()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns whether command blocks are enabled on the (entire) server

### BroadcastChat(Message, ExcludeClient, ChatPrefix)

| Name | Type | Notes |
| --- | --- | --- |
| Message | string |  |
| ExcludeClient (optional) | cClientHandle |  |
| ChatPrefix (optional) | eMessageType |  |

Sends the Message to all players in this world, except the optional ExcludeClient. No formatting is done by the server.

### BroadcastChatDeath(Message, ExcludeClient)

| Name | Type | Notes |
| --- | --- | --- |
| Message | string |  |
| ExcludeClient (optional) | cClientHandle |  |

Prepends Gray [DEATH] / colours entire text (depending on ShouldUseChatPrefixes()) and broadcasts message. For when a player dies.

### BroadcastChatFailure(Message, ExcludeClient)

| Name | Type | Notes |
| --- | --- | --- |
| Message | string |  |
| ExcludeClient (optional) | cClientHandle |  |

Prepends Rose [INFO] / colours entire text (depending on ShouldUseChatPrefixes()) and broadcasts message. For a command that failed to run because of insufficient permissions, etc.

### BroadcastChatFatal(Message, ExcludeClient)

| Name | Type | Notes |
| --- | --- | --- |
| Message | string |  |
| ExcludeClient (optional) | cClientHandle |  |

Prepends Red [FATAL] / colours entire text (depending on ShouldUseChatPrefixes()) and broadcasts message. For a plugin that crashed, or similar.

### BroadcastChatInfo(Message, ExcludeClient)

| Name | Type | Notes |
| --- | --- | --- |
| Message | string |  |
| ExcludeClient (optional) | cClientHandle |  |

Prepends Yellow [INFO] / colours entire text (depending on ShouldUseChatPrefixes()) and broadcasts message. For informational messages, such as command usage.

### BroadcastChatSuccess(Message, ExcludeClient)

| Name | Type | Notes |
| --- | --- | --- |
| Message | string |  |
| ExcludeClient (optional) | cClientHandle |  |

Prepends Green [INFO] / colours entire text (depending on ShouldUseChatPrefixes()) and broadcasts message. For success messages.

### BroadcastChatWarning(Message, ExcludeClient)

| Name | Type | Notes |
| --- | --- | --- |
| Message | string |  |
| ExcludeClient (optional) | cClientHandle |  |

Prepends Rose [WARN] / colours entire text (depending on ShouldUseChatPrefixes()) and broadcasts message. For concerning events, such as plugin reload etc.

### BroadcastEntityAnimation(TargetEntity, Animation, ExcludeClient)

| Name | Type | Notes |
| --- | --- | --- |
| TargetEntity | cEntity |  |
| Animation | number |  |
| ExcludeClient (optional) | cClientHandle |  |

Sends an animation of an entity to all clienthandles (except ExcludeClient if given)

### BroadcastPlayerListHeaderFooter(Header, Footer)

| Name | Type | Notes |
| --- | --- | --- |
| Header | cCompositeChat |  |
| Footer | cCompositeChat |  |

### ChangeWeather()

Forces the weather to change in the next game tick. Weather is changed according to the normal rules: wSunny <-> wRain <-> wStorm

### ChunkStay(ChunkCoordTable, OnChunkAvailable, OnAllChunksAvailable)

| Name | Type | Notes |
| --- | --- | --- |
| ChunkCoordTable | table |  |
| OnChunkAvailable (optional) | function |  |
| OnAllChunksAvailable (optional) | function |  |

Queues the specified chunks to be loaded or generated and calls the specified callbacks once they are loaded. ChunkCoordTable is an arra-table of chunk coords, each coord being a table of 2 numbers: { {Chunk1x, Chunk1z}, {Chunk2x, Chunk2z}, ...}. When any of those chunks are made available (including being available at the start of this call), the OnChunkAvailable() callback is called. When all the chunks are available, the OnAllChunksAvailable() callback is called. The function signatures are: <pre class="prettyprint lang-lua">function OnChunkAvailable(ChunkX, ChunkZ)function OnAllChunksAvailable()</pre> All return values from the callbacks are ignored.

### CreateProjectile(X, Y, Z, ProjectileKind, Creator, Originating Item, Speed)

| Name | Type | Notes |
| --- | --- | --- |
| X | number |  |
| Y | number |  |
| Z | number |  |
| ProjectileKind | cProjectileEntity#eKind |  |
| Creator | cEntity |  |
| Originating Item | cItem |  |
| Speed (optional) | Vector3d |  |

Creates a new projectile of the specified kind at the specified coords. The projectile's creator is set to Creator (may be nil). The item that created the projectile entity, commonly the {{cPlayer|player}}'s currently equipped item, is used at present for fireworks to correctly set their entity metadata. It is not used for any other projectile. Optional speed indicates the initial speed for the projectile.

### Overload 1: DigBlock(X, Y, Z, Digger)

| Name | Type | Notes |
| --- | --- | --- |
| X | number |  |
| Y | number |  |
| Z | number |  |
| Digger (optional) | cEntity |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Replaces the specified block with air, without dropping the usual pickups for the block. Wakes up the simulators for the block and its neighbors. The optional Digger parameter specifies the entity who dug the block, usually a player. Returns true on success, or false if the chunk is not loaded or invalid coords. See also DropBlockAsPickups() for the version that drops pickups.

### Overload 2: DigBlock(BlockPos, Digger)

| Name | Type | Notes |
| --- | --- | --- |
| BlockPos | Vector3i |  |
| Digger (optional) | cEntity |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Replaces the specified block with air, without dropping the usual pickups for the block. Wakes up the simulators for the block and its neighbors. The optional Digger parameter specifies the entity who dug the block, usually a player. Returns true on success, or false if the chunk is not loaded or invalid coords. See also DropBlockAsPickups() for the version that drops pickups.

### DoExplosionAt(Force, X, Y, Z, CanCauseFire, Source, SourceData)

| Name | Type | Notes |
| --- | --- | --- |
| Force | number |  |
| X | number |  |
| Y | number |  |
| Z | number |  |
| CanCauseFire | boolean |  |
| Source | eExplosionSource |  |
| SourceData | any |  |

Creates an explosion of the specified relative force in the specified position. If CanCauseFire is set, the explosion will set blocks on fire, too. The Source parameter specifies the source of the explosion, one of the esXXX constants. The SourceData parameter is specific to each source type, usually it provides more info about the source.

### DoWithBeaconAt(BlockX, BlockY, BlockZ, CallbackFunction)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockY | number |  |
| BlockZ | number |  |
| CallbackFunction | function |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

If there is a beacon at the specified coords, calls the CallbackFunction with the {{cBeaconEntity}} parameter representing the beacon. The CallbackFunction has the following signature: <pre class="prettyprint lang-lua">function Callback({{cBeaconEntity|BeaconEntity}})</pre> The function returns false if there is no beacon, or if there is, it returns the bool value that the callback has returned.

### DoWithBedAt(BlockX, BlockY, BlockZ, CallbackFunction)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockY | number |  |
| BlockZ | number |  |
| CallbackFunction | function |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

If there is a bed at the specified coords, calls the CallbackFunction with the {{cBedEntity}} parameter representing the bed. The CallbackFunction has the following signature: <pre class="prettyprint lang-lua">function Callback({{cBedEntity|cBedEntity}})</pre> The function returns false if there is no bed, or if there is, it returns the bool value that the callback has returned.

### DoWithBlockEntityAt(BlockX, BlockY, BlockZ, CallbackFunction)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockY | number |  |
| BlockZ | number |  |
| CallbackFunction | function |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

If there is a block entity at the specified coords, calls the CallbackFunction with the {{cBlockEntity}} parameter representing the block entity. The CallbackFunction has the following signature: <pre class="prettyprint lang-lua">function Callback({{cBlockEntity|BlockEntity}})</pre> The function returns false if there is no block entity, or if there is, it returns the bool value that the callback has returned.

### DoWithBrewingstandAt(BlockX, BlockY, BlockZ, CallbackFunction)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockY | number |  |
| BlockZ | number |  |
| CallbackFunction | function |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

If there is a brewingstand at the specified coords, calls the CallbackFunction with the {{cBrewingstandEntity}} parameter representing the brewingstand. The CallbackFunction has the following signature: <pre class="prettyprint lang-lua">function Callback({{cBrewingstandEntity|cBrewingstandEntity}})</pre> The function returns false if there is no brewingstand, or if there is, it returns the bool value that the callback has returned.

### DoWithChestAt(BlockX, BlockY, BlockZ, CallbackFunction)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockY | number |  |
| BlockZ | number |  |
| CallbackFunction | function |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

If there is a chest at the specified coords, calls the CallbackFunction with the {{cChestEntity}} parameter representing the chest. The CallbackFunction has the following signature: <pre class="prettyprint lang-lua">function Callback({{cChestEntity|ChestEntity}})</pre> The function returns false if there is no chest, or if there is, it returns the bool value that the callback has returned.

### DoWithCommandBlockAt(BlockX, BlockY, BlockZ, CallbackFunction)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockY | number |  |
| BlockZ | number |  |
| CallbackFunction | function |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

If there is a command block at the specified coords, calls the CallbackFunction with the {{cCommandBlockEntity}} parameter representing the command block. The CallbackFunction has the following signature: <pre class="prettyprint lang-lua">function Callback({{cCommandBlockEntity|CommandBlockEntity}})</pre> The function returns false if there is no command block, or if there is, it returns the bool value that the callback has returned.

### DoWithDispenserAt(BlockX, BlockY, BlockZ, CallbackFunction)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockY | number |  |
| BlockZ | number |  |
| CallbackFunction | function |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

If there is a dispenser at the specified coords, calls the CallbackFunction with the {{cDispenserEntity}} parameter representing the dispenser. The CallbackFunction has the following signature: <pre class="prettyprint lang-lua">function Callback({{cDispenserEntity|DispenserEntity}})</pre> The function returns false if there is no dispenser, or if there is, it returns the bool value that the callback has returned.

### DoWithDropSpenserAt(BlockX, BlockY, BlockZ, CallbackFunction)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockY | number |  |
| BlockZ | number |  |
| CallbackFunction | function |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

If there is a dropper or a dispenser at the specified coords, calls the CallbackFunction with the {{cDropSpenserEntity}} parameter representing the dropper or dispenser. The CallbackFunction has the following signature: <pre class="prettyprint lang-lua">function Callback({{cDropSpenserEntity|DropSpenserEntity}})</pre> Note that this can be used to access both dispensers and droppers in a similar way. The function returns false if there is neither dispenser nor dropper, or if there is, it returns the bool value that the callback has returned.

### DoWithDropperAt(BlockX, BlockY, BlockZ, CallbackFunction)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockY | number |  |
| BlockZ | number |  |
| CallbackFunction | function |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

If there is a dropper at the specified coords, calls the CallbackFunction with the {{cDropperEntity}} parameter representing the dropper. The CallbackFunction has the following signature: <pre class="prettyprint lang-lua">function Callback({{cDropperEntity|DropperEntity}})</pre> The function returns false if there is no dropper, or if there is, it returns the bool value that the callback has returned.

### DoWithEntityByID(EntityID, CallbackFunction)

| Name | Type | Notes |
| --- | --- | --- |
| EntityID | number |  |
| CallbackFunction | function |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

If an entity with the specified ID exists, calls the callback with the {{cEntity}} parameter representing the entity. The CallbackFunction has the following signature: <pre class="prettyprint lang-lua">function Callback({{cEntity|Entity}})</pre> The function returns false if the entity was not found, and it returns the same bool value that the callback has returned if the entity was found.

### DoWithFlowerPotAt(BlockX, BlockY, BlockZ, CallbackFunction)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockY | number |  |
| BlockZ | number |  |
| CallbackFunction | function |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

If there is a flower pot at the specified coords, calls the CallbackFunction with the {{cFlowerPotEntity}} parameter representing the flower pot. The CallbackFunction has the following signature: <pre class="prettyprint lang-lua">function Callback({{cFlowerPotEntity|FlowerPotEntity}})</pre> The function returns false if there is no flower pot, or if there is, it returns the bool value that the callback has returned.

### DoWithFurnaceAt(BlockX, BlockY, BlockZ, CallbackFunction)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockY | number |  |
| BlockZ | number |  |
| CallbackFunction | function |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

If there is a furnace at the specified coords, calls the CallbackFunction with the {{cFurnaceEntity}} parameter representing the furnace. The CallbackFunction has the following signature: <pre class="prettyprint lang-lua">function Callback({{cFurnaceEntity|FurnaceEntity}})</pre> The function returns false if there is no furnace, or if there is, it returns the bool value that the callback has returned.

### DoWithHopperAt(BlockX, BlockY, BlockZ, CallbackFunction)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockY | number |  |
| BlockZ | number |  |
| CallbackFunction | function |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

If there is a hopper at the specified coords, calls the CallbackFunction with the {{cHopperEntity}} parameter representing the hopper. The CallbackFunction has the following signature: <pre class="prettyprint lang-lua">function Callback({{cHopperEntity|cHopperEntity}})</pre> The function returns false if there is no hopper, or if there is, it returns the bool value that the callback has returned.

### DoWithMobHeadAt(BlockX, BlockY, BlockZ, CallbackFunction)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockY | number |  |
| BlockZ | number |  |
| CallbackFunction | function |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

If there is a mob head at the specified coords, calls the CallbackFunction with the {{cMobHeadEntity}} parameter representing the furnace. The CallbackFunction has the following signature: <pre class="prettyprint lang-lua">function Callback({{cMobHeadEntity|MobHeadEntity}})</pre> The function returns false if there is no mob head, or if there is, it returns the bool value that the callback has returned.

### DoWithNearestPlayer(Position, RangeLimit, CallbackFunction, CheckLineOfSight, IgnoreSpectator)

| Name | Type | Notes |
| --- | --- | --- |
| Position | Vector3d |  |
| RangeLimit | number |  |
| CallbackFunction | function |  |
| CheckLineOfSight | boolean |  |
| IgnoreSpectator | boolean |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Calls the specified callback function with the {{cPlayer|player}} nearest to the specified position as its parameter, if they are still within the range limit. The CallbackFunction has the following signature: <pre class="prettyprint lang-lua">function Callback({{cPlayer|Player}})</pre> The function returns false if the player was not found, or whatever bool value the callback returned if the player was found.

### DoWithNoteBlockAt(BlockX, BlockY, BlockZ, CallbackFunction)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockY | number |  |
| BlockZ | number |  |
| CallbackFunction | function |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

If there is a note block at the specified coords, calls the CallbackFunction with the {{cNoteEntity}} parameter representing the note block. The CallbackFunction has the following signature: <pre class="prettyprint lang-lua">function Callback({{cNoteEntity|NoteEntity}})</pre> The function returns false if there is no note block, or if there is, it returns the bool value that the callback has returned.

### DoWithPlayer(PlayerName, CallbackFunction)

| Name | Type | Notes |
| --- | --- | --- |
| PlayerName | string |  |
| CallbackFunction | function |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

If there is a player of the specified name (exact match), calls the CallbackFunction with the {{cPlayer}} parameter representing the player. The CallbackFunction has the following signature: <pre class="prettyprint lang-lua">function Callback({{cPlayer|Player}})</pre> The function returns false if the player was not found, or whatever bool value the callback returned if the player was found.

### DoWithPlayerByUUID(PlayerUUID, CallbackFunction)

| Name | Type | Notes |
| --- | --- | --- |
| PlayerUUID | cUUID |  |
| CallbackFunction | function |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

If there is the player with the uuid, calls the CallbackFunction with the {{cPlayer}} parameter representing the player. The CallbackFunction has the following signature: <pre class="prettyprint lang-lua">function Callback({{cPlayer|Player}})</pre> The function returns false if the player was not found, or whatever bool value the callback returned if the player was found.

### DropBlockAsPickups(BlockPos, Digger, Tool)

| Name | Type | Notes |
| --- | --- | --- |
| BlockPos | Vector3i |  |
| Digger (optional) | cEntity |  |
| Tool (optional) | cItem |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| IsSuccess | boolean |  |

Digs up the specified block and spawns the appropriate pickups for it. The optional Digger parameter specifies the {{cEntity|entity}} who dug the block, usually a {{cPlayer|player}}. The optional Tool parameter specifies the tool used to dig the block, not present means an empty hand. Returns true on success, false if the chunk is not present. See also DigBlock() for the pickup-less version.

### Overload 1: FastSetBlock(BlockX, BlockY, BlockZ, BlockType, BlockMeta)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockY | number |  |
| BlockZ | number |  |
| BlockType | number |  |
| BlockMeta | number |  |

Sets the block at the specified coords, without waking up the simulators or replacing the block entities for the previous block type. Do not use if the block being replaced has a block entity tied to it! <b>OBSOLETE</b>, use the vector-based overload instead.

### Overload 2: FastSetBlock(BlockCoords, BlockType, BlockMeta)

| Name | Type | Notes |
| --- | --- | --- |
| BlockCoords | Vector3i |  |
| BlockType | number |  |
| BlockMeta | number |  |

Sets the block at the specified coords, without waking up the simulators or replacing the block entities for the previous block type. Do not use if the block being replaced has a block entity tied to it!

### FindAndDoWithPlayer(PlayerName, CallbackFunction)

| Name | Type | Notes |
| --- | --- | --- |
| PlayerName | string |  |
| CallbackFunction | function |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Calls the given callback function for the player with the name best matching the name string provided.<br>This function is case-insensitive and will match partial names.<br>Returns false if player not found or there is ambiguity, true otherwise. The CallbackFunction has the following signature: <pre class="prettyprint lang-lua">function Callback({{cPlayer|Player}})</pre>

### ForEachBlockEntityInChunk(ChunkX, ChunkZ, CallbackFunction)

| Name | Type | Notes |
| --- | --- | --- |
| ChunkX | number |  |
| ChunkZ | number |  |
| CallbackFunction | function |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Calls the specified callback for each block entity in the chunk. Returns true if all block entities in the chunk have been processed (including when there are zero block entities), or false if the callback has aborted the enumeration by returning true. The CallbackFunction has the following signature: <pre class="prettyprint lang-lua">function Callback({{cBlockEntity|BlockEntity}})</pre> The callback should return false or no value to continue with the next block entity, or true to abort the enumeration.

### ForEachBrewingstandInChunk(ChunkX, ChunkZ, CallbackFunction)

| Name | Type | Notes |
| --- | --- | --- |
| ChunkX | number |  |
| ChunkZ | number |  |
| CallbackFunction | function |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Calls the specified callback for each brewingstand in the chunk. Returns true if all brewingstands in the chunk have been processed (including when there are zero brewingstands), or false if the callback has aborted the enumeration by returning true. The CallbackFunction has the following signature: <pre class="prettyprint lang-lua">function Callback({{cBrewingstandEntity|cBrewingstandEntity}})</pre> The callback should return false or no value to continue with the next brewingstand, or true to abort the enumeration.

### ForEachChestInChunk(ChunkX, ChunkZ, CallbackFunction)

| Name | Type | Notes |
| --- | --- | --- |
| ChunkX | number |  |
| ChunkZ | number |  |
| CallbackFunction | function |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Calls the specified callback for each chest in the chunk. Returns true if all chests in the chunk have been processed (including when there are zero chests), or false if the callback has aborted the enumeration by returning true. The CallbackFunction has the following signature: <pre class="prettyprint lang-lua">function Callback({{cChestEntity|ChestEntity}})</pre> The callback should return false or no value to continue with the next chest, or true to abort the enumeration.

### ForEachEntity(CallbackFunction)

| Name | Type | Notes |
| --- | --- | --- |
| CallbackFunction | function |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Calls the specified callback for each entity in the loaded world. Returns true if all the entities have been processed (including when there are zero entities), or false if the callback function has aborted the enumeration by returning true. The callback function has the following signature: <pre class="prettyprint lang-lua">function Callback({{cEntity|Entity}})</pre> The callback should return false or no value to continue with the next entity, or true to abort the enumeration.

### ForEachEntityInBox(Box, CallbackFunction)

| Name | Type | Notes |
| --- | --- | --- |
| Box | cBoundingBox |  |
| CallbackFunction | function |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Calls the specified callback for each entity in the specified bounding box. Returns true if all the entities have been processed (including when there are zero entities), or false if the callback function has aborted the enumeration by returning true. If any chunk within the bounding box is not valid, it is silently skipped without any notification. The callback function has the following signature: <pre class="prettyprint lang-lua">function Callback({{cEntity|Entity}})</pre> The callback should return false or no value to continue with the next entity, or true to abort the enumeration.

### ForEachEntityInChunk(ChunkX, ChunkZ, CallbackFunction)

| Name | Type | Notes |
| --- | --- | --- |
| ChunkX | number |  |
| ChunkZ | number |  |
| CallbackFunction | function |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Calls the specified callback for each entity in the specified chunk. Returns true if all the entities have been processed (including when there are zero entities), or false if the chunk is not loaded or the callback function has aborted the enumeration by returning true. The callback function has the following signature: <pre class="prettyprint lang-lua">function Callback({{cEntity|Entity}})</pre> The callback should return false or no value to continue with the next entity, or true to abort the enumeration.

### ForEachFurnaceInChunk(ChunkX, ChunkZ, CallbackFunction)

| Name | Type | Notes |
| --- | --- | --- |
| ChunkX | number |  |
| ChunkZ | number |  |
| CallbackFunction | function |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Calls the specified callback for each furnace in the chunk. Returns true if all furnaces in the chunk have been processed (including when there are zero furnaces), or false if the callback has aborted the enumeration by returning true. The CallbackFunction has the following signature: <pre class="prettyprint lang-lua">function Callback({{cFurnaceEntity|FurnaceEntity}})</pre> The callback should return false or no value to continue with the next furnace, or true to abort the enumeration.

### ForEachLoadedChunk(CallbackFunction)

| Name | Type | Notes |
| --- | --- | --- |
| CallbackFunction | function |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Calls the specified callback for each loaded chunk in the world. Returns true if all chunks have been processed, or false if the callback has aborted the enumeration by returning true. The CallbackFunction has the following signature: <pre class="prettyprint lang-lua">function Callback(ChunkX, ChunkZ)</pre> The callback should return false or no value to continue with the next chunk, or true to abort the enumeration.

### ForEachPlayer(CallbackFunction)

| Name | Type | Notes |
| --- | --- | --- |
| CallbackFunction | function |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Calls the specified callback for each player in the loaded world. Returns true if all the players have been processed (including when there are zero players), or false if the callback function has aborted the enumeration by returning true. The callback function has the following signature: <pre class="prettyprint lang-lua">function Callback({{cPlayer|Player}})</pre> The callback should return false or no value to continue with the next player, or true to abort the enumeration.

### GenerateChunk(ChunkX, ChunkZ)

| Name | Type | Notes |
| --- | --- | --- |
| ChunkX | number |  |
| ChunkZ | number |  |

Queues the specified chunk in the chunk generator. Ignored if the chunk is already generated (use RegenerateChunk() to force chunk re-generation).

### GetBiomeAt(BlockX, BlockZ)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockZ | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| eBiome | EMCSBiome |  |

Returns the biome at the specified coords. Reads the biome from the chunk, if it is loaded, otherwise it uses the chunk generator to provide the biome value.

### Overload 1: GetBlock(BlockX, BlockY, BlockZ)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockY | number |  |
| BlockZ | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| BLOCKTYPE | number |  |

Returns the block type of the block at the specified coords, or 0 if the appropriate chunk is not loaded. <b>OBSOLETE</b>, use the vector-based overload instead.

### Overload 2: GetBlock(BlockCoords)

| Name | Type | Notes |
| --- | --- | --- |
| BlockCoords | Vector3i |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| BLOCKTYPE | number |  |

Returns the block type of the block at the specified coords, or 0 if the appropriate chunk is not loaded.

### Overload 1: GetBlockBlockLight(BlockX, BlockY, BlockZ)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockY | number |  |
| BlockZ | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the amount of block light at the specified coords, or 0 if the appropriate chunk is not loaded. <b>OBSOLETE</b>, use the vector-based overload instead.

### Overload 2: GetBlockBlockLight(Pos)

| Name | Type | Notes |
| --- | --- | --- |
| Pos | Vector3i |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the amount of block light at the specified coords, or 0 if the appropriate chunk is not loaded.

### GetBlockInfo(BlockX, BlockY, BlockZ)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockY | number |  |
| BlockZ | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| IsBlockValid | boolean |  |
| BlockType | number |  |
| BlockMeta | number |  |
| BlockSkyLight | number |  |
| BlockBlockLight | number |  |

Returns the complete block info for the block at the specified coords. The first value specifies if the block is in a valid loaded chunk, the other values are valid only if BlockValid is true.

### Overload 1: GetBlockMeta(BlockX, BlockY, BlockZ)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockY | number |  |
| BlockZ | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the block metadata of the block at the specified coords, or 0 if the appropriate chunk is not loaded. <b>OBSOLETE</b>, use the vector-based overload instead.

### Overload 2: GetBlockMeta(BlockCoords)

| Name | Type | Notes |
| --- | --- | --- |
| BlockCoords | Vector3i |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the block metadata of the block at the specified coords, or 0 if the appropriate chunk is not loaded.

### GetBlockSkyLight(BlockX, BlockY, BlockZ)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockY | number |  |
| BlockZ | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the block skylight of the block at the specified coords, or 0 if the appropriate chunk is not loaded.

### GetBlockTypeMeta(BlockX, BlockY, BlockZ)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockY | number |  |
| BlockZ | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| IsBlockValid | boolean |  |
| BlockType | number |  |
| BlockMeta | number |  |

Returns the block type and metadata for the block at the specified coords. The first value specifies if the block is in a valid loaded chunk, the other values are valid only if BlockValid is true.

### GetDataPath()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | string |  |

Returns the path to the root of the world data.

### GetDefaultWeatherInterval(Weather)

| Name | Type | Notes |
| --- | --- | --- |
| Weather | eWeather |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the default weather interval for the specific weather type. Returns -1 for any unknown weather.

### GetDimension()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | eDimension |  |

Returns the dimension of the world - dimOverworld, dimNether or dimEnd.

### GetGameMode()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | eGameMode |  |

Returns the gamemode of the world - gmSurvival, gmCreative or gmAdventure.

### GetGeneratorQueueLength()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the number of chunks that are queued in the chunk generator.

### GetHeight(BlockX, BlockZ)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockZ | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

<b>DEPRECATED</b>, use TryGetHeight instead. Returns the maximum height of the particular block column in the world. If the chunk is not loaded, this function used to block until the chunk was loaded, leading to possible deadlock. Now it returns 0 instead.

### GetIniFileName()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | string |  |

Returns the name of the world.ini file that the world uses to store the information.

### GetLightingQueueLength()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the number of chunks in the lighting thread's queue.

### GetLinkedEndWorldName()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | string |  |

Returns the name of the end world this world is linked to.

### GetLinkedNetherWorldName()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | string |  |

Returns the name of the Netherworld linked to this world.

### GetLinkedOverworldName()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | string |  |

Returns the name of the world this world is linked to.

### GetMapManager()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | cMapManager |  |

Returns the {{cMapManager|MapManager}} object used by this world.

### GetMaxCactusHeight()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the configured maximum height to which cacti will grow naturally.

### GetMaxNetherPortalHeight()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the maximum height for a nether portal

### GetMaxNetherPortalWidth()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the maximum width for a nether portal

### GetMaxSugarcaneHeight()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the configured maximum height to which sugarcane will grow naturally.

### GetMaxViewDistance()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the maximum viewdistance that players can see in this world. The view distance is the amount of chunks around the player that the player can see.

### GetMinNetherPortalHeight()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the minimum height for a nether portal

### GetMinNetherPortalWidth()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the minimum width for a nether portal

### GetName()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | string |  |

Returns the name of the world, as specified in the settings.ini file.

### GetNumChunks()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the number of chunks currently loaded.

### GetNumUnusedDirtyChunks()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the number of unused dirty chunks. That's the number of chunks that we can save and then unload.

### GetScoreBoard()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | cScoreboard |  |

Returns the {{cScoreboard|Scoreboard}} object used by this world. 

### GetSeed()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the seed of the world.

### GetSignLines(BlockX, BlockY, BlockZ)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockY | number |  |
| BlockZ | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| IsValid | boolean |  |
| Line1 | string |  |
| Line2 | string |  |
| Line3 | string |  |
| Line4 | string |  |

Returns true and the lines of a sign at the specified coords, or false if there is no sign at the coords.

### GetSpawnPos()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | Vector3d |  |

Returns the default spawn position

### GetSpawnX()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the X coord of the default spawn

### GetSpawnY()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the Y coord of the default spawn

### GetSpawnZ()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the Z coord of the default spawn

### GetStorageLoadQueueLength()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the number of chunks queued up for loading

### GetStorageSaveQueueLength()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the number of chunks queued up for saving

### GetTNTShrapnelLevel()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| ShrapnelLevel | eShrapnelLevel |  |

Returns the shrapnel level, representing the block types that are propelled outwards following an explosion. Based on this value and a random picker, blocks are selectively converted to physics entities (FallingSand) and flung outwards.

### GetTicksUntilWeatherChange()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the number of ticks that will pass before the weather is changed

### GetTimeOfDay()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the number of ticks that have passed from the sunrise, 0 .. 24000.

### GetWeather()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | eWeather |  |

Returns the current weather in the world (wSunny, wRain, wStorm). To check for weather, use IsWeatherXXX() functions instead.

### GetWorldAge()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the total age of the world, in ticks. The age always grows, cannot be set by plugins and is unrelated to TimeOfDay.

### GrowPlantAt(BlockPos, NumStages)

| Name | Type | Notes |
| --- | --- | --- |
| BlockPos | Vector3i |  |
| NumStages | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Grows the plant at the specified block by the specified number of stages. Returns the number of stages actually grown. Returns zero for non-growable blocks.

### GrowRipePlant(BlockPos)

| Name | Type | Notes |
| --- | --- | --- |
| BlockPos | Vector3i |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Grows the plant at the specified coords to maturity. Returns true if the plant was grown, false if not.

### GrowTree(BlockPos)

| Name | Type | Notes |
| --- | --- | --- |
| BlockPos | Vector3i |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Grows a tree based at the specified coords. If there is a sapling there, grows the tree based on that sapling, otherwise chooses a tree image based on the biome. Returns true if the tree was grown, false if not (invalid chunk, insufficient space)

### GrowTreeByBiome(BlockPos)

| Name | Type | Notes |
| --- | --- | --- |
| BlockPos | Vector3i |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Grows a tree based at the specified coords. The tree type is picked from types available for the biome at those coords. Returns true if the tree was grown, false if not (invalid chunk, insufficient space)

### GrowTreeFromSapling(BlockPos)

| Name | Type | Notes |
| --- | --- | --- |
| BlockPos | Vector3i |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Grows a tree based at the specified coords. The tree type is determined from the sapling meta. If the sapling is part of a 2x2 sapling area, grows a large tree. Returns true if the tree was grown, false if not (invalid chunk, insufficient space)

### IsBlockDirectlyWatered(BlockX, BlockY, BlockZ)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockY | number |  |
| BlockZ | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if the specified block has a water block right next to it (on the X/Z axes)

### IsDaylightCycleEnabled()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if the daylight cycle is enabled.

### IsDeepSnowEnabled()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns whether the configuration has DeepSnow enabled.

### IsFarmlandTramplingEnabled()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if farmland trampling is enabled.

### IsGameModeAdventure()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if the current gamemode is gmAdventure.

### IsGameModeCreative()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if the current gamemode is gmCreative.

### IsGameModeSpectator()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if the current gamemode is gmSpectator.

### IsGameModeSurvival()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if the current gamemode is gmSurvival.

### IsPVPEnabled()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns whether PVP is enabled in the world settings.

### IsSavingEnabled()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns whether or not saving chunk data is enabled. If disabled, the world will keep dirty chunks in memory forever, and will simply regenerate non-dirty chunks that are unloaded.

### IsSlimeChunk(ChunkX, ChunkZ)

| Name | Type | Notes |
| --- | --- | --- |
| ChunkX | number |  |
| ChunkZ | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns whether slimes can spawn in the chunk.

### IsTrapdoorOpen(BlockX, BlockY, BlockZ)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockY | number |  |
| BlockZ | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns false if there is no trapdoor there or if the block isn't a trapdoor or if the chunk wasn't loaded. Returns true if trapdoor is open.

### IsWeatherRain()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if the current weather is rainy.

### IsWeatherRainAt(BlockX, BlockZ)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockZ | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if it is rainy at the specified location. This takes into account biomes.

### IsWeatherStorm()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if the current weather is stormy.

### IsWeatherStormAt(BlockX, BlockZ)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockZ | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if it is stormy at the specified location. This takes into account biomes.

### IsWeatherSunny()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if the current weather is sunny.

### IsWeatherSunnyAt(BlockX, BlockZ)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockZ | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if it is sunny at the specified location. This takes into account biomes.

### IsWeatherWet()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if the world currently has any precipitation - rain, storm or snow.

### IsWeatherWetAt(BlockX, BlockZ)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockZ | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if it is raining or storming at the specified location. This takes into account biomes.

### IsWeatherWetAtXYZ(Pos)

| Name | Type | Notes |
| --- | --- | --- |
| Pos | Vector3i |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if the specified location has wet weather (rain or storm), using the same logic as IsWeatherWetAt, except that any rain-blocking blocks above the specified position will block the precipitation and this function will return false. Note if the chunk is unloaded then the weather state for the world will be returned.

### PickupsFromBlock(BlockPos, Digger, Tool)

| Name | Type | Notes |
| --- | --- | --- |
| BlockPos | Vector3i |  |
| Digger (optional) | cEntity |  |
| Tool (optional) | cItem |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| Items | cItems |  |

Returns all the pickups that would result if the Digger dug up the block at BlockPos using Tool. Digger is usually a {{cPlayer}}, but can be nil for natural causes. Tool is usually the equipped {{cItem|item}}, can be nil for empty hand. Returns an empty {{cItems}} object if the chunk is not present.

### PrepareChunk(ChunkX, ChunkZ, Callback)

| Name | Type | Notes |
| --- | --- | --- |
| ChunkX | number |  |
| ChunkZ | number |  |
| Callback (optional) | function |  |

Queues the chunk for preparing - making sure that it's generated and lit. It is legal to call with no callback. The callback function has the following signature: <pre class="prettyprint lang-lua">function Callback(ChunkX, ChunkZ)</pre>

### QueueBlockForTick(BlockX, BlockY, BlockZ, TicksToWait)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockY | number |  |
| BlockZ | number |  |
| TicksToWait | number |  |

Queues the specified block to be ticked after the specified number of gameticks.

### QueueSaveAllChunks()

Queues all chunks to be saved in the world storage thread

### QueueTask(TaskFunction)

| Name | Type | Notes |
| --- | --- | --- |
| TaskFunction | function |  |


					Queues the specified function to be executed in the tick thread. This is the primary means
					of interaction with a cWorld from the WebAdmin page handlers (see {{WebWorldThreads}}). The function
					signature is <pre class=\"pretty-print lang-lua\">function({{cWorld|World}})</pre>All return values
					from the function are ignored. Note that this function is actually called *after* the QueueTask()
					function returns. Note that it is unsafe to store references to Cuberite objects, such as entities,
					across from the caller to the task handler function; store the EntityID instead.
				

### QueueUnloadUnusedChunks()

Queues a cTask that unloads chunks that are no longer needed and are saved.

### RegenerateChunk(ChunkX, ChunkZ)

| Name | Type | Notes |
| --- | --- | --- |
| ChunkX | number |  |
| ChunkZ | number |  |

Queues the specified chunk to be re-generated, overwriting the current data. To queue a chunk for generating only if it doesn't exist, use the GenerateChunk() instead.

### ScheduleTask(DelayTicks, TaskFunction)

| Name | Type | Notes |
| --- | --- | --- |
| DelayTicks | number |  |
| TaskFunction | function |  |

Queues the specified function to be executed in the world's tick thread after a the specified number of ticks. This enables operations to be queued for execution in the future. The function signature is <pre class="pretty-print lang-lua">function({{cWorld|World}})</pre>All return values from the function are ignored. Note that it is unsafe to store references to Cuberite objects, such as entities, across from the caller to the task handler function; store the EntityID instead.

### SendBlockTo(BlockX, BlockY, BlockZ, Player)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockY | number |  |
| BlockZ | number |  |
| Player | cPlayer |  |

Sends the block at the specified coords to the specified player's client, as an UpdateBlock packet.

### Overload 1: SetAreaBiome(MinX, MaxX, MinZ, MaxZ, Biome)

| Name | Type | Notes |
| --- | --- | --- |
| MinX | number |  |
| MaxX | number |  |
| MinZ | number |  |
| MaxZ | number |  |
| Biome | EMCSBiome |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Sets the biome in the rectangular area specified. Returns true if successful, false if any of the chunks were unloaded.

### Overload 2: SetAreaBiome(Cuboid, Biome)

| Name | Type | Notes |
| --- | --- | --- |
| Cuboid | cCuboid |  |
| Biome | EMCSBiome |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Sets the biome in the cuboid specified. Returns true if successful, false if any of the chunks were unloaded. The cuboid needn't be sorted.

### SetBiomeAt(BlockX, BlockZ, Biome)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockZ | number |  |
| Biome | EMCSBiome |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Sets the biome at the specified block coords. Returns true if successful, false otherwise.

### SetBlock(BlockX, BlockY, BlockZ, BlockType, BlockMeta)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockY | number |  |
| BlockZ | number |  |
| BlockType | number |  |
| BlockMeta | number |  |

Sets the block at the specified coords, replaces the block entities for the previous block type, creates a new block entity for the new block, if appropriate, and wakes up the simulators. This is the preferred way to set blocks, as opposed to FastSetBlock(), which is only to be used under special circumstances.

### Overload 1: SetBlockMeta(BlockX, BlockY, BlockZ, BlockMeta)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockY | number |  |
| BlockZ | number |  |
| BlockMeta | number |  |

Sets the meta for the block at the specified coords. Any call to SetBlockMeta will not generate a simulator update (water, lava, redstone), consider using SetBlock instead.

### Overload 2: SetBlockMeta(BlockCoords, BlockMeta)

| Name | Type | Notes |
| --- | --- | --- |
| BlockCoords | Vector3i |  |
| BlockMeta | number |  |

Sets the meta for the block at the specified coords. Any call to SetBlockMeta will not generate a simulator update (water, lava, redstone), consider using SetBlock instead.

### SetChunkAlwaysTicked(ChunkX, ChunkZ, IsAlwaysTicked)

| Name | Type | Notes |
| --- | --- | --- |
| ChunkX | number |  |
| ChunkZ | number |  |
| IsAlwaysTicked | boolean |  |

Sets the chunk to always be ticked and loaded even when it doesn't contain any clients. IsAlwaysTicked set to true turns forced ticking on, set to false turns it off. Every call with 'true' should be paired with a later call with 'false', otherwise the ticking won't stop. Multiple actions can request ticking independently, the ticking will continue until the last call with 'false'.

### SetCommandBlockCommand(BlockX, BlockY, BlockZ, Command)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockY | number |  |
| BlockZ | number |  |
| Command | string |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Sets the command to be executed in a command block at the specified coordinates. Returns if command was changed.

### SetCommandBlocksEnabled(AreEnabled)

| Name | Type | Notes |
| --- | --- | --- |
| AreEnabled | boolean |  |

Sets whether command blocks should be enabled on the (entire) server.

### SetDaylightCycleEnabled(IsEnabled)

| Name | Type | Notes |
| --- | --- | --- |
| IsEnabled | boolean |  |

Starts or stops the daylight cycle.

### SetLinkedEndWorldName(WorldName)

| Name | Type | Notes |
| --- | --- | --- |
| WorldName | string |  |

Sets the name of the world that the end portal should link to.

### SetLinkedNetherWorldName(WorldName)

| Name | Type | Notes |
| --- | --- | --- |
| WorldName | string |  |

Sets the name of the world that the nether portal should link to.

### SetLinkedOverworldName(WorldName)

| Name | Type | Notes |
| --- | --- | --- |
| WorldName | string |  |

Sets the name of the world that the nether portal should link to?

### SetMaxNetherPortalHeight(Height)

| Name | Type | Notes |
| --- | --- | --- |
| Height | number |  |

Sets the maximum height for a nether portal

### SetMaxNetherPortalWidth(Width)

| Name | Type | Notes |
| --- | --- | --- |
| Width | number |  |

Sets the maximum width for a nether portal

### SetMaxViewDistance(MaxViewDistance)

| Name | Type | Notes |
| --- | --- | --- |
| MaxViewDistance | number |  |

Sets the maximum viewdistance of the players in the world. This maximum takes precedence over each player's ViewDistance setting.

### SetMinNetherPortalHeight(Height)

| Name | Type | Notes |
| --- | --- | --- |
| Height | number |  |

Sets the minimum height for a nether portal

### SetMinNetherPortalWidth(Width)

| Name | Type | Notes |
| --- | --- | --- |
| Width | number |  |

Sets the minimum width for a nether portal

### SetNextBlockTick(BlockX, BlockY, BlockZ)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockY | number |  |
| BlockZ | number |  |

DEPRECATED, use SetNextBlockToTick() instead.

### SetNextBlockToTick(BlockPos)

| Name | Type | Notes |
| --- | --- | --- |
| BlockPos | Vector3i |  |

Requests that the specified block be ticked at the start of the next world tick. Only one block per chunk can be queued this way; a second call to the same chunk overwrites the previous call.

### SetSavingEnabled(SavingEnabled)

| Name | Type | Notes |
| --- | --- | --- |
| SavingEnabled | boolean |  |

Sets whether saving chunk data is enabled. If disabled, dirty chunks will stay in memory forever, which may cause performance and stability issues.

### SetShouldUseChatPrefixes(ShouldUseChatPrefixes)

| Name | Type | Notes |
| --- | --- | --- |
| ShouldUseChatPrefixes | boolean |  |

Sets whether coloured chat prefixes such as [INFO] is used with the SendMessageXXX() or BroadcastChatXXX(), or simply the entire message is coloured in the respective colour.

### SetSignLines(BlockX, BlockY, BlockZ, Line1, Line2, Line3, Line4, Player)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockY | number |  |
| BlockZ | number |  |
| Line1 | string |  |
| Line2 | string |  |
| Line3 | string |  |
| Line4 | string |  |
| Player (optional) | cPlayer |  |

Sets the sign text at the specified coords. The sign-updating hooks are called for the change. The Player parameter is used to indicate the player from whom the change has come, it may be nil.

### SetSpawn(X, Y, Z)

| Name | Type | Notes |
| --- | --- | --- |
| X | number |  |
| Y | number |  |
| Z | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Sets the default spawn at the specified coords. Returns false if the new spawn couldn't be stored in the INI file.

### SetTNTShrapnelLevel(ShrapnelLevel)

| Name | Type | Notes |
| --- | --- | --- |
| ShrapnelLevel | eShrapnelLevel |  |

Sets the Shrapnel level of the world.

### SetTicksUntilWeatherChange(NumTicks)

| Name | Type | Notes |
| --- | --- | --- |
| NumTicks | number |  |

Sets the number of ticks after which the weather will be changed.

### SetTimeOfDay(TimeOfDayTicks)

| Name | Type | Notes |
| --- | --- | --- |
| TimeOfDayTicks | number |  |

Sets the time of day, expressed as number of ticks past sunrise, in the range 0 .. 24000.

### SetTrapdoorOpen(BlockX, BlockY, BlockZ, IsOpen)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockY | number |  |
| BlockZ | number |  |
| IsOpen | boolean |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Opens or closes a trapdoor at the specific coordinates. Returns true on success, false if there is no trapdoor or it's already in the requested state.

### SetWeather(Weather)

| Name | Type | Notes |
| --- | --- | --- |
| Weather | eWeather |  |

Sets the current weather (wSunny, wRain, wStorm) and resets the TicksUntilWeatherChange to the default value for the new weather. The normal weather-changing hooks are called for the change.

### ShouldBroadcastAchievementMessages()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if the server should broadcast achievement messages in this world.

### ShouldBroadcastDeathMessages()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if the server should broadcast death messages in this world.

### ShouldLavaSpawnFire()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if the world is configured to spawn fires near lava (world.ini: [Physics].ShouldLavaSpawnFire value)

### ShouldUseChatPrefixes()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns whether coloured chat prefixes are prepended to chat messages or the entire message is simply coloured.

### Overload 1: SpawnBoat(Position, Material)

| Name | Type | Notes |
| --- | --- | --- |
| Position | Vector3d |  |
| Material | cBoat#eMaterial |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| EntityID | number |  |

Spawns a {{cBoat|boat}} at the specific coordinates. Returns the EntityID of the new boat, or {{cEntity#INVALID_ID|cEntity#INVALID_ID}} if no boat was created.

### Overload 2: SpawnBoat(X, Y, Z, Material)

| Name | Type | Notes |
| --- | --- | --- |
| X | number |  |
| Y | number |  |
| Z | number |  |
| Material | cBoat#eMaterial |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| EntityID | number |  |

Spawns a {{cBoat|boat}} at the specific coordinates. Returns the EntityID of the new boat, or {{cEntity#INVALID_ID|cEntity#INVALID_ID}} if no boat was created. (DEPRECATED, use vector-parametered version)

### SpawnEnderCrystal(Pos, ShowBottom)

| Name | Type | Notes |
| --- | --- | --- |
| Pos | Vector3d |  |
| ShowBottom | boolean |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| EntityID | number |  |

Spawns an {{cEnderCrystal|ender crystal}} at the specified coords. Returns the EntityID of the new ender crystal, or {{cEntity#INVALID_ID|cEntity#INVALID_ID}} if no ender crystal was created.

### SpawnExperienceOrb(X, Y, Z, Reward)

| Name | Type | Notes |
| --- | --- | --- |
| X | number |  |
| Y | number |  |
| Z | number |  |
| Reward | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| EntityID | number |  |

Spawns an {{cExpOrb|experience orb}} at the specified coords, with the given reward. Returns the EntityID of the new experience orb, or {{cEntity#INVALID_ID|cEntity#INVALID_ID}} if no experience orb was created.

### Overload 1: SpawnFallingBlock(X, Y, Z, BlockType, BlockMeta)

| Name | Type | Notes |
| --- | --- | --- |
| X | number |  |
| Y | number |  |
| Z | number |  |
| BlockType | number |  |
| BlockMeta | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| EntityID | number |  |

OBSOLETE, use the Vector3-based overloads instead. Spawns a {{cFallingBlock|Falling Block}} entity at the specified coords with the given block type/meta. Returns the EntityID of the new falling block, or {{cEntity#INVALID_ID|cEntity#INVALID_ID}} if no falling block was created.

### Overload 2: SpawnFallingBlock(BlockPos, BlockType, BlockMeta)

| Name | Type | Notes |
| --- | --- | --- |
| BlockPos | Vector3i |  |
| BlockType | number |  |
| BlockMeta | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| EntityID | number |  |

Spawns a {{cFallingBlock|Falling Block}} entity in the middle of the specified block, with the given block type/meta. Returns the EntityID of the new falling block, or {{cEntity#INVALID_ID|cEntity#INVALID_ID}} if no falling block was created.

### Overload 3: SpawnFallingBlock(Pos, BlockType, BlockMeta)

| Name | Type | Notes |
| --- | --- | --- |
| Pos | Vector3d |  |
| BlockType | number |  |
| BlockMeta | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| EntityID | number |  |

Spawns a {{cFallingBlock|Falling Block}} entity at exactly the specified coords, with the given block type/meta. Returns the EntityID of the new falling block, or {{cEntity#INVALID_ID|cEntity#INVALID_ID}} if no falling block was created.

### SpawnItemPickup(PosX, PosY, PosZ, Item, SpeedX, SpeedY, SpeedZ, LifetimeTicks, CanCombine)

| Name | Type | Notes |
| --- | --- | --- |
| PosX | number |  |
| PosY | number |  |
| PosZ | number |  |
| Item | cItem |  |
| SpeedX (optional) | number | Speed along X coordinate to spawn with. Default is 0. |
| SpeedY (optional) | number | Speed along Y coordinate to spawn with. Default is 0. |
| SpeedZ (optional) | number | Speed along Z coordinate to spawn with. Default is 0. |
| LifetimeTicks (optional) | number | Length of the pickups lifetime, in ticks. Default 5 minutes (6000 ticks) |
| CanCombine (optional) | boolean | Whether this pickup is allowed to combine with other similar pickups. |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| EntityID | number |  |

Creates a single pickup entity of the given item at the given position with the given speed, and returns the entities unique ID.

### Overload 1: SpawnItemPickups(Pickups, X, Y, Z, FlyAwaySpeed, IsPlayerCreated)

| Name | Type | Notes |
| --- | --- | --- |
| Pickups | cItems |  |
| X | number |  |
| Y | number |  |
| Z | number |  |
| FlyAwaySpeed (optional) | number |  |
| IsPlayerCreated (optional) | boolean |  |

Spawns the specified pickups at the position specified. The FlyAwaySpeed is a coefficient (default: 1) used to initialize the random speed in which the pickups fly away from the spawn position. The IsPlayerCreated parameter (default: false) is used to initialize the created {{cPickup}} object's IsPlayerCreated value.

### Overload 2: SpawnItemPickups(Pickups, X, Y, Z, SpeedX, SpeedY, SpeedZ, IsPlayerCreated)

| Name | Type | Notes |
| --- | --- | --- |
| Pickups | cItems |  |
| X | number |  |
| Y | number |  |
| Z | number |  |
| SpeedX | number |  |
| SpeedY | number |  |
| SpeedZ | number |  |
| IsPlayerCreated (optional) | boolean |  |

Spawns the specified pickups at the position specified. All the pickups fly away from the spawn position using the specified speed. The IsPlayerCreated parameter (default: false) is used to initialize the created {{cPickup}} object's IsPlayerCreated value.

### SpawnMinecart(X, Y, Z, MinecartType, Item, BlockHeight)

| Name | Type | Notes |
| --- | --- | --- |
| X | number |  |
| Y | number |  |
| Z | number |  |
| MinecartType | number |  |
| Item (optional) | cItem |  |
| BlockHeight (optional) | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| EntityID | number |  |

Spawns a minecart at the specific coordinates. MinecartType is the item type of the minecart. If the minecart is an empty minecart then the given Item (default: empty) is the block to be displayed inside the minecart, and BlockHeight (default: 1) is the relative distance of the block from the minecart. Returns the EntityID of the new minecart, or {{cEntity#INVALID_ID|cEntity#INVALID_ID}} if no minecart was created.

### SpawnMob(X, Y, Z, MonsterType, IsBaby)

| Name | Type | Notes |
| --- | --- | --- |
| X | number |  |
| Y | number |  |
| Z | number |  |
| MonsterType | eMonsterType |  |
| IsBaby (optional) | boolean |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| EntityID | number |  |

Spawns the specified type of mob at the specified coords. If the Baby parameter is true, the mob will be a baby. Returns the EntityID of the created entity, or {{cEntity#INVALID_ID|cEntity#INVALID_ID}} on failure.

### Overload 1: SpawnPrimedTNT(Position, FuseTicks, InitialVelocityCoeff, ShouldPlayFuseSound)

| Name | Type | Notes |
| --- | --- | --- |
| Position | Vector3d |  |
| FuseTicks | number |  |
| InitialVelocityCoeff | number |  |
| ShouldPlayFuseSound | boolean |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| EntityID | number |  |

Spawns a {{cTNTEntity|primed TNT entity}} at the specified coords, with the given fuse ticks. The entity gets a random speed multiplied by the InitialVelocityCoeff, 1 being the default value. Returns the EntityID of the new spawned primed tnt, or {{cEntity#INVALID_ID|cEntity#INVALID_ID}} if no primed tnt was created.

### Overload 2: SpawnPrimedTNT(X, Y, Z, FuseTicks, InitialVelocityCoeff)

| Name | Type | Notes |
| --- | --- | --- |
| X | number |  |
| Y | number |  |
| Z | number |  |
| FuseTicks | number |  |
| InitialVelocityCoeff | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| EntityID | number |  |

Spawns a {{cTNTEntity|primed TNT entity}} at the specified coords, with the given fuse ticks. The entity gets a random speed multiplied by the InitialVelocityCoeff, 1 being the default value. Returns the EntityID of the new spawned primed tnt, or {{cEntity#INVALID_ID|cEntity#INVALID_ID}} if no primed tnt was created. (DEPRECATED, use vector-parametered version)

### SpawnSplitExperienceOrbs(Position, Reward)

| Name | Type | Notes |
| --- | --- | --- |
| Position | Vector3d |  |
| Reward | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| EntityID | table |  |

Spawns experience orbs of the specified total value at the given location. The orbs' values are split according to regular Minecraft rules. Returns an array-table of UniqueID of all the orbs.

### TryGetHeight(BlockX, BlockZ)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockZ | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| IsValid | boolean |  |
| Height | number |  |

Returns true and height of the highest non-air block if the chunk is loaded, or false otherwise.

### UpdateSign(BlockX, BlockY, BlockZ, Line1, Line2, Line3, Line4, Player)

| Name | Type | Notes |
| --- | --- | --- |
| BlockX | number |  |
| BlockY | number |  |
| BlockZ | number |  |
| Line1 | string |  |
| Line2 | string |  |
| Line3 | string |  |
| Line4 | string |  |
| Player (optional) | cPlayer |  |

(<b>DEPRECATED</b>) Please use SetSignLines().

### UseBlockEntity(Player, BlockX, BlockY, BlockZ)

| Name | Type | Notes |
| --- | --- | --- |
| Player | cPlayer |  |
| BlockX | number |  |
| BlockY | number |  |
| BlockZ | number |  |

Makes the specified Player use the block entity at the specified coords (open chest UI, etc.) If the cords are in an unloaded chunk or there's no block entity, ignores the call.

### VillagersShouldHarvestCrops()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if villagers can harvest crops.

### WakeUpSimulators(Block)

| Name | Type | Notes |
| --- | --- | --- |
| Block | Vector3i |  |

Wakes up the simulators for the specified block.

### WakeUpSimulatorsInArea(Area)

| Name | Type | Notes |
| --- | --- | --- |
| Area | cCuboid |  |

Wakes up the simulators for all the blocks in the specified area (edges inclusive).

## Additional Info

### Using callbacks

To avoid problems with stale objects, the cWorld class will not let plugins get a direct pointer
to an {{cEntity|entity}}, {{cBlockEntity|block entity}} or a {{cPlayer|player}}. Such an object
could be modified or even destroyed by another thread while the plugin holds it, so it would be
rather unsafe.

Instead, the cWorld provides access to these objects using callbacks. The plugin provides a
function that is called and receives the object as a parameter; cWorld guarantees that while
the callback is executing, the object will stay valid. If a plugin needs to "remember" the
object outside of the callback, it needs to store the entity ID, blockentity coords or player
name.

The following code examples show how to use the callbacks

This code teleports player Player to another player named ToName in the same world:

```
-- Player is a cPlayer object
-- ToName is a string
-- World is a cWorld object
World:ForEachPlayer(
	function (a_OtherPlayer)
	if (a_OtherPlayer:GetName() == ToName) then
		Player:TeleportToEntity(a_OtherPlayer);
	end
);
```

This code fills each furnace in the chunk with 64 coals:

```
-- Player is a cPlayer object
-- World is a cWorld object
World:ForEachFurnaceInChunk(Player:GetChunkX(), Player:GetChunkZ(),
	function (a_Furnace)
		a_Furnace:SetFuelSlot(cItem(E_ITEM_COAL, 64));
	end
);
```

This code teleports all spiders up by 100 blocks:

```
-- World is a cWorld object
World:ForEachEntity(
	function (a_Entity)
		if not(a_Entity:IsMob()) then
			return;
		end

		-- Now that we know the entity represents a mob, we can use cMonster functions:
		if (a_Entity:GetMobType() == mtSpider) then
			a_Entity:TeleportToCoords(a_Entity:GetPosX(), a_Entity:GetPosY() + 100, a_Entity:GetPosZ());
		end
	end
);
```
