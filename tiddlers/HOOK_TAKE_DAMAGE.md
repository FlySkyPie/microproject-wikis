This hook is called when any {{cEntity}} descendant, such as a {{cPlayer|player}} or a
{{cMonster|mob}}, takes any kind of damage. The plugins may modify the amount of damage or effects
with this hook by editting the {{TakeDamageInfo}} object passed.

This hook is called after the final damage is calculated, including all the possible weapon
{{cEnchantments|enchantments}}, armor protection and potion effects.

## Callback function

The default name for the callback function is OnTakeDamage. It has the following signature:

```lua
function MyOnTakeDamage(Receiver, TDI)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| Receiver | [cEntity](#cEntity) | The entity taking damage |
| TDI | [TakeDamageInfo](#TakeDamageInfo) | The damage type, cause and effects. Plugins may modify this object to alter the final damage applied. |

If the function returns false or no value, other plugins' callbacks are called and then the server
applies the final values from the TDI object to Receiver. If the function returns true, no other
callbacks are called, and no damage nor effects are applied.
