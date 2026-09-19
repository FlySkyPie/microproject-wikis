This callback gets called whenever a block is about to be dug. This includes {{cPlayer|players}}
digging blocks, entities causing blocks to disappear ({{cTNTEntity|TNT}}, Endermen) and natural
causes (water washing away a block). Plugins may override the amount and kinds of pickups this
action produces.

## Callback function

The default name for the callback function is OnBlockToPickups. It has the following signature:

```lua
function MyOnBlockToPickups(World, Digger, BlockX, BlockY, BlockZ, BlockType, BlockMeta, Pickups)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| World | [cWorld](#cWorld) | The world in which the block resides |
| Digger | [cEntity](#cEntity) | The entity causing the digging. May be a {{cPlayer}}, {{cTNTEntity}} or even nil (natural causes) |
| BlockX | number | X-coord of the block |
| BlockY | number | Y-coord of the block |
| BlockZ | number | Z-coord of the block |
| BlockType | BLOCKTYPE | Block type of the block |
| BlockMeta | NIBBLETYPE | Block meta of the block |
| Pickups | [cItems](#cItems) | Items that will be spawned as pickups |

If the function returns false or no value, the next callback in the hook chain will be called. If
the function returns true, no other callbacks in the chain will be called.

Either way, the server will then spawn pickups specified in the Pickups parameter, so to disable
pickups, you need to Clear the object first, then return true.
