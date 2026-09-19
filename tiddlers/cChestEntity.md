**Inherits from:** [cBlockEntityWithItems](#cBlockEntityWithItems)

A chest entity is a {{cBlockEntityWithItems|cBlockEntityWithItems}} descendant that represents a chest
in the world. Note that doublechests consist of two separate cChestEntity objects, they do not collaborate
in any way.

To manipulate a chest already in the game, you need to use {{cWorld}}'s callback mechanism with
either DoWithChestAt() or ForEachChestInChunk() function. See the code example below

## Constants

| Name | Notes |
| --- | --- |
| ContentsHeight | Height of the contents' {{cItemGrid|ItemGrid}}, as required by the parent class, {{cBlockEntityWithItems}} |
| ContentsWidth | Width of the contents' {{cItemGrid|ItemGrid}}, as required by the parent class, {{cBlockEntityWithItems}} |

## Additional Info

### Code example

The following example code sets the top-left item of each chest in the same chunk as Player to
64 \* diamond:

```
-- Player is a {{cPlayer}} object instance
local World = Player:GetWorld();
World:ForEachChestInChunk(Player:GetChunkX(), Player:GetChunkZ(),
	function (ChestEntity)
		ChestEntity:SetSlot(0, 0, cItem(E_ITEM_DIAMOND, 64));
	end
);
```
