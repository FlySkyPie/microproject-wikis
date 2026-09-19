This callback gets called when the server finishes loading and initializing plugins. This is the
perfect occasion for a plugin to query other plugins through {{cPluginManager}}:GetPlugin() and
possibly start communicating with them using the {{cPlugin}}:Call() function.

## Callback function

The default name for the callback function is OnPluginsLoaded. It has the following signature:

```lua
function MyOnPluginsLoaded()
```

The return value is ignored, all registered callbacks are called.
