This hook is called after an explosion has been processed in a world.

See also {{OnExploding|HOOK_EXPLODING}} for a similar hook called before the explosion.

The explosion carries with it the type of its source - whether it's a creeper exploding, or TNT,
etc. It also carries the identification of the actual source. The exact type of the identification
depends on the source kind, see the {{Globals#ExplosionSource|esXXX}} constants' descriptions for details.

## Callback function

The default name for the callback function is OnExploded. It has the following signature:

```lua
function MyOnExploded(World, ExplosionSize, CanCauseFire, X, Y, Z, Source, SourceData)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| World | [cWorld](#cWorld) | The world where the explosion happened |
| ExplosionSize | number | The relative explosion size |
| CanCauseFire | bool | True if the explosion has turned random air blocks to fire (such as a ghast fireball) |
| X | number | X-coord of the explosion center |
| Y | number | Y-coord of the explosion center |
| Z | number | Z-coord of the explosion center |
| Source | eExplosionSource | Source of the explosion. See the table above. |
| SourceData | varies | Additional data for the source. The exact type varies by the source. See the {{Globals#ExplosionSource|esXXX}} constants' descriptions. |

If the function returns false or no value, the next plugin's callback is called. If the function
returns true, no other callback is called for this event. There is no overridable behaviour.
