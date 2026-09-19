This hook is called when the {{cPlayer|player}} shoots their bow. It is called for the actual
release of the {{cArrowEntity|arrow}}. FIXME: It is currently unknown whether other
{{cProjectileEntity|projectiles}} (snowballs, eggs) trigger this hook.

To get the player's position and direction, use the {{cPlayer}}:GetEyePosition() and
cPlayer:GetLookVector() functions. Note that for shooting a bow, the position for the arrow creation
is not at the eye pos, some adjustments are required. FIXME: Export the {{cPlayer}} function for
this adjustment.

## Callback function

The default name for the callback function is OnPlayerShooting. It has the following signature:

```lua
function MyOnPlayerShooting(Player)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| Player | [cPlayer](#cPlayer) | The player shooting |

If the function returns false or no value, the next plugin's callback is called, and finally
Cuberite creates the projectile. If the functino returns true, no other callback is called and no
projectile is created.
