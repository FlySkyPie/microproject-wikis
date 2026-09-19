**Inherits from:** [cBlockEntity](#cBlockEntity)

This class represents a mob spawner block entity in the world.

## Functions

### GetEntity()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| MobType | eMonsterType |  |

Returns the entity type that will be spawn by this mob spawner.

### GetMaxNearbyEntities()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the maximum number of entities of the same type that can be present before the spawner cannot spawn more entities.

### GetMaxSpawnDelay()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the maximum number of ticks the spawner waits until spawning new entities automatically.

### GetMinSpawnDelay()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the minimum number of ticks the spawner waits until spawning new entities automatically.

### GetNearbyMonsterNum(MobType)

| Name | Type | Notes |
| --- | --- | --- |
| MobType | eMonsterType |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the amount of this monster type in a radius defined by SetSpawnRange (Y: 4-block radius).

### GetNearbyPlayersNum()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the amount of the nearby players in a 16-block radius.

### GetRequiredPlayerRange()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the maximum euclidean distance from a player where the spawner can be activated.

### GetSpawnCount()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the number of entities the spawner will try to spawn on each activation.

### GetSpawnDelay()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the spawn delay. This is the tick delay that is needed to spawn new monsters.

### GetSpawnRange()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns half the length of the square the spawner tries to spawn entities in.

### ResetTimer()

Sets the spawn delay to a new random value.

### SetEntity(MobType)

| Name | Type | Notes |
| --- | --- | --- |
| MobType | eMonsterType |  |

Sets the type of the mob that will be spawned by this mob spawner.

### SetMaxNearbyEntities(MaxNearbyEntities)

| Name | Type | Notes |
| --- | --- | --- |
| MaxNearbyEntities | number |  |

Sets the maximum amount of nearby entities until the spawner will stop spawning this entity type.

### SetMaxSpawnDelay(MaxSpawnDelay)

| Name | Type | Notes |
| --- | --- | --- |
| MaxSpawnDelay | number |  |

Sets the maximum amount of ticks the spawner will wait before spawning new entities.

### SetMinSpawnDelay(MinSpawnDelay)

| Name | Type | Notes |
| --- | --- | --- |
| MinSpawnDelay | number |  |

Sets the minimum amount of ticks the spawner will wait before spawning new entities.

### SetRequiredPlayerRange(RequiredPlayerRange)

| Name | Type | Notes |
| --- | --- | --- |
| RequiredPlayerRange | number |  |

Sets the maximum euclidean distance from a player where the spawner can be activated.

### SetSpawnCount(SpawnCount)

| Name | Type | Notes |
| --- | --- | --- |
| SpawnCount | number |  |

Sets the number of entities the spawner will try to spawn in each activation. Might not spawn all of them due to spawn limitations of the entity.

### SetSpawnDelay(SpawnDelayTicks)

| Name | Type | Notes |
| --- | --- | --- |
| SpawnDelayTicks | number |  |

Sets the spawn delay.

### SetSpawnRange(SpawnRange)

| Name | Type | Notes |
| --- | --- | --- |
| SpawnRange | number |  |

Sets half the length of the square the spawner will try to spawn entities in.

### SpawnEntity()

Spawns the entity. NOTE: This function resets the delay before the next automatic activation of the spawner.

### UpdateActiveState()

Update the active flag from the mob spawner. This function is called every 5 seconds from the Tick() function.
