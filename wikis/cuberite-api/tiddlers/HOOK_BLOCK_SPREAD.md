This hook is called when a block spreads.

The spread carries with it the type of its source - whether it's a block spreads.
It also carries the identification of the actual source. The exact type of the identification
depends on the source kind:

| Source | Notes |
| --- | --- |
| ssFireSpread | Fire spreading |
| ssGrassSpread | Grass spreading |
| ssMushroomSpread | Mushroom spreading |
| ssMycelSpread | Mycel spreading |
| ssVineSpread | Vine spreading |

## Callback function

The default name for the callback function is OnBlockSpread. It has the following signature:

```lua
function MyOnBlockSpread(World, BlockX, BlockY, BlockZ, Source)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| World | [cWorld](#cWorld) | The world in which the block resides |
| BlockX | number | X-coord of the block |
| BlockY | number | Y-coord of the block |
| BlockZ | number | Z-coord of the block |
| Source | eSpreadSource | Source of the spread. See the table above. |

If the function returns false or no value, the next plugin's callback is called, and finally
Cuberite will process the spread. If the function
returns true, no other callback is called for this event and the spread will not occur.

## Code examples

### Stop fire spreading

Stops fire from spreading, but does not remove any player-placed fire.

```lua
function OnBlockSpread(World, BlockX, Blocky, BlockZ, source)
	if (source == ssFireSpread) then
		-- Return true to block the fire spreading.
		return true
	end
	-- We don't care about any other events, let them continue.
	return false
end

-- Add the callback.
cPluginManager:AddHook(cPluginManager.HOOK_BLOCK_SPREAD, OnBlockSpread);
```
