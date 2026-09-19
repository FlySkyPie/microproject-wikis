This hook is called before an explosion has been processed in a world.

See also {{OnExploded|HOOK_EXPLODED}} for a similar hook called after the explosion.

The explosion carries with it the type of its source - whether it's a creeper exploding, or TNT,
etc. It also carries the identification of the actual source. The exact type of the identification
depends on the source kind, see the {{Globals#ExplosionSource|esXXX}} constants' descriptions for details

## Callback function

The default name for the callback function is OnExploding. It has the following signature:

```lua
function MyOnExploding(World, ExplosionSize, CanCauseFire, X, Y, Z, Source, SourceData)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| World | [cWorld](#cWorld) | The world where the explosion happens |
| ExplosionSize | number | The relative explosion size |
| CanCauseFire | bool | True if the explosion will turn random air blocks to fire (such as a ghast fireball) |
| X | number | X-coord of the explosion center |
| Y | number | Y-coord of the explosion center |
| Z | number | Z-coord of the explosion center |
| Source | eExplosionSource | Source of the explosion. See the table above. |
| SourceData | varies | Additional data for the source. The exact type varies by the source. See the {{Globals#ExplosionSource|esXXX}} constants' description. |

If the function returns false or no value, the next plugin's callback is called, and finally
Cuberite will process the explosion - destroy blocks and push + hurt entities. If the function
returns true, no other callback is called for this event and the explosion will not occur.

The hook handler may return up to two more values after the initial bool. The second returned value
overrides the CanCauseFire parameter for subsequent hook calls and the final explosion, the third
returned value overrides the ExplosionSize parameter for subsequent hook calls and the final explosion.
