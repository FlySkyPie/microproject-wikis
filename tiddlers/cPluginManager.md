This class is used for generic plugin-related functionality. The plugin manager has a list of all
plugins, can enable or disable plugins, manages hooks and in-game console commands.

Plugins can be identified by either the PluginFolder or PluginName. Note that these two can differ,
refer to [the forum](https://forum.cuberite.org/thread-1877.html) for detailed discussion.

There is one instance of cPluginManager in Cuberite, to get it, call either
{{cRoot|cRoot}}:Get():GetPluginManager() or cPluginManager:Get() function.

Note that some functions are "static", that means that they are called using a dot operator instead
of the colon operator. For example:

```
cPluginManager.AddHook(cPluginManager.HOOK_CHAT, OnChatMessage);
```

## Functions

### **Static** AddHook(HookType, [Callback])

| Name | Type | Notes |
| --- | --- | --- |
| HookType | cPluginManager#PluginHook |  |
| Callback (optional) | function |  |

Informs the plugin manager that it should call the specified function when the specified hook event occurs. If a function is not specified, a default global function name is looked up, based on the hook type

### Overload 1: BindCommand(Command, Permission, Callback, HelpString)

| Name | Type | Notes |
| --- | --- | --- |
| Command | string |  |
| Permission | string |  |
| Callback | function |  |
| HelpString | string |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Binds an in-game command with the specified callback function, permission and help string. By common convention, providing an empty string for HelpString will hide the command from the /help display. Returns true if successful, logs to console and returns no value on error. The callback uses the following signature: <pre class="prettyprint lang-lua">function(Split, {{cPlayer|Player}})</pre> The Split parameter contains an array-table of the words that the player has sent, Player is the {{cPlayer}} object representing the player who sent the command. If the callback returns true, the command is assumed to have executed successfully; in all other cases the server sends a warning to the player that the command is unknown (this is so that subcommands can be implemented).

### Overload 2: **Static** BindCommand(Command, Permission, Callback, HelpString)

| Name | Type | Notes |
| --- | --- | --- |
| Command | string |  |
| Permission | string |  |
| Callback | function |  |
| HelpString | string |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Binds an in-game command with the specified callback function, permission and help string. By common convention, providing an empty string for HelpString will hide the command from the /help display. Returns true if successful, logs to console and returns no value on error. The callback uses the following signature: <pre class="prettyprint lang-lua">function(Split, {{cPlayer|Player}})</pre> The Split parameter contains an array-table of the words that the player has sent, Player is the {{cPlayer}} object representing the player who sent the command. If the callback returns true, the command is assumed to have executed successfully; in all other cases the server sends a warning to the player that the command is unknown (this is so that subcommands can be implemented).

### Overload 1: **Static** BindConsoleCommand(Command, Callback, HelpString)

| Name | Type | Notes |
| --- | --- | --- |
| Command | string |  |
| Callback | function |  |
| HelpString | string |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Binds a console command with the specified callback function and help string. By common convention, providing an empty string for HelpString will hide the command from the "help" console command. Returns true if successful, logs to console and returns no value on error. The callback uses the following signature: <pre class="prettyprint lang-lua">function(Split)</pre> The Split parameter contains an array-table of the words that the admin has typed. If the callback returns true, the command is assumed to have executed successfully; in all other cases the server issues a warning to the console that the command is unknown (this is so that subcommands can be implemented).

### Overload 2: BindConsoleCommand(Command, Callback, HelpString)

| Name | Type | Notes |
| --- | --- | --- |
| Command | string |  |
| Callback | function |  |
| HelpString | string |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Binds a console command with the specified callback function and help string. By common convention, providing an empty string for HelpString will hide the command from the "help" console command. Returns true if successful, logs to console and returns no value on error. The callback uses the following signature: <pre class="prettyprint lang-lua">function(Split)</pre> The Split parameter contains an array-table of the words that the admin has typed. If the callback returns true, the command is assumed to have executed successfully; in all other cases the server issues a warning to the console that the command is unknown (this is so that subcommands can be implemented).

### **Static** CallPlugin(PluginName, FunctionName, [FunctionArgs...])

| Name | Type | Notes |
| --- | --- | --- |
| PluginName | string |  |
| FunctionName | string |  |
| FunctionArgs... (optional) | ... |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| FunctionRets | ... |  |

Calls the specified function in the specified plugin, passing all the given arguments to it. If it succeeds, it returns all the values returned by that function. If it fails, returns no value at all. Note that only strings, numbers, bools, nils, API classes and simple tables can be used for parameters and return values; functions cannot be copied across plugins.

### **Static** DoWithPlugin(PluginName, CallbackFn)

| Name | Type | Notes |
| --- | --- | --- |
| PluginName | string |  |
| CallbackFn | function |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Calls the CallbackFn for the specified plugin, if found. A plugin can be found even if it is currently unloaded, disabled or errored, the callback should check the plugin status. If the plugin is not found, this function returns false, otherwise it returns the bool value that the callback has returned. The CallbackFn has the following signature: <pre class="prettyprint lang-lua">function ({{cPlugin|Plugin}})</pre>

### ExecuteCommand(Player, CommandStr)

| Name | Type | Notes |
| --- | --- | --- |
| Player | cPlayer |  |
| CommandStr | string |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| CommandResult | cPluginManager#CommandResult |  |

Executes the command as if given by the specified Player. Checks permissions.

### ExecuteConsoleCommand(CommandStr)

| Name | Type | Notes |
| --- | --- | --- |
| CommandStr | string |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |
|  | string |  |

Executes the console command as if given by the admin on the console. If the command is successfully executed, returns true and the text that would be output to the console normally. On error it returns false and an error message.

### FindPlugins()

<b>OBSOLETE</b>, use RefreshPluginList() instead

### ForEachCommand(CallbackFn)

| Name | Type | Notes |
| --- | --- | --- |
| CallbackFn | function |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Calls the CallbackFn function for each command that has been bound using BindCommand(). The CallbackFn has the following signature: <pre class="prettyprint lang-lua">function(Command, Permission, HelpString)</pre> If the callback returns true, the enumeration is aborted and this API function returns false; if it returns false or no value, the enumeration continues with the next command, and the API function returns true.

### ForEachConsoleCommand(CallbackFn)

| Name | Type | Notes |
| --- | --- | --- |
| CallbackFn | function |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Calls the CallbackFn function for each command that has been bound using BindConsoleCommand(). The CallbackFn has the following signature: <pre class="prettyprint lang-lua">function (Command, HelpString)</pre> If the callback returns true, the enumeration is aborted and this API function returns false; if it returns false or no value, the enumeration continues with the next command, and the API function returns true.

### Overload 1: **Static** ForEachPlugin(CallbackFn)

| Name | Type | Notes |
| --- | --- | --- |
| CallbackFn | function |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Calls the CallbackFn function for each plugin that is currently discovered by Cuberite (including disabled, unloaded and errrored plugins). The CallbackFn has the following signature: <pre class="prettyprint lang-lua">function ({{cPlugin|Plugin}})</pre> If the callback returns true, the enumeration is aborted and this API function returns false; if it returns false or no value, the enumeration continues with the next command, and the API function returns true.

### Overload 2: ForEachPlugin(CallbackFn)

| Name | Type | Notes |
| --- | --- | --- |
| CallbackFn | function |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Calls the CallbackFn function for each plugin that is currently discovered by Cuberite (including disabled, unloaded and errrored plugins). The CallbackFn has the following signature: <pre class="prettyprint lang-lua">function ({{cPlugin|Plugin}})</pre> If the callback returns true, the enumeration is aborted and this API function returns false; if it returns false or no value, the enumeration continues with the next command, and the API function returns true.

### ForceExecuteCommand(Player, CommandStr)

| Name | Type | Notes |
| --- | --- | --- |
| Player | cPlayer |  |
| CommandStr | string |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| CommandResult | cPluginManager#CommandResult |  |

Same as ExecuteCommand, but doesn't check permissions

### **Static** Get()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | cPluginManager |  |

Returns the single instance of the plugin manager

### GetAllPlugins()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | table |  |

Returns a table (dictionary) of all plugins, [name => value], where value is a valid {{cPlugin}} if the plugin is loaded, or the bool value false if the plugin is not loaded.

### GetCommandPermission(Command)

| Name | Type | Notes |
| --- | --- | --- |
| Command | string |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| Permission | string |  |

Returns the permission needed for executing the specified command

### GetCurrentPlugin()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | cPlugin |  |

Returns the {{cPlugin}} object for the calling plugin. This is the same object that the Initialize function receives as the argument.

### GetNumLoadedPlugins()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the number of loaded plugins (psLoaded only)

### GetNumPlugins()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the number of plugins, including the disabled, errored, unloaded and not-found ones

### GetPlugin(PluginName)

| Name | Type | Notes |
| --- | --- | --- |
| PluginName | string |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | cPlugin |  |

(<b>DEPRECATED, UNSAFE</b>) Returns a plugin handle of the specified plugin, or nil if such plugin is not loaded. Note thatdue to multithreading the handle is not guaranteed to be safe for use when stored - a single-plugin reload may have been triggered in the mean time for the requested plugin.

### GetPluginFolderName(PluginName)

| Name | Type | Notes |
| --- | --- | --- |
| PluginName | string |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | string |  |

Returns the name of the folder from which the plugin was loaded (without the "Plugins" part). Used as a plugin's display name.

### **Static** GetPluginsPath()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | string |  |

Returns the path where the individual plugin folders are located. Doesn't include the path separator at the end of the returned string.

### IsCommandBound(Command)

| Name | Type | Notes |
| --- | --- | --- |
| Command | string |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if in-game Command is already bound (by any plugin)

### IsConsoleCommandBound(Command)

| Name | Type | Notes |
| --- | --- | --- |
| Command | string |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if console Command is already bound (by any plugin)

### IsPluginLoaded(PluginName)

| Name | Type | Notes |
| --- | --- | --- |
| PluginName | string |  |

Returns true if the specified plugin is loaded.

### LoadPlugin(PluginFolder)

| Name | Type | Notes |
| --- | --- | --- |
| PluginFolder | string |  |

(<b>DEPRECATED</b>) Loads a plugin from the specified folder. NOTE: Loading plugins may be an unsafe operation and may result in a deadlock or a crash. This API is deprecated and might be removed.

### **Static** LogStackTrace()

Logs a current stack trace of the Lua engine to the server console log. Same format as is used when the plugin fails.

### RefreshPluginList()

Refreshes the list of plugins to include all folders inside the Plugins folder (potentially new disabled plugins)

### ReloadPlugin(PluginName)

| Name | Type | Notes |
| --- | --- | --- |
| PluginName | string |  |

Queues the specified plugin to be reloaded. To avoid deadlocks, the reloading happens in the main tick thread asynchronously.

### ReloadPlugins()

Reloads all active plugins

### UnloadPlugin(PluginName)

| Name | Type | Notes |
| --- | --- | --- |
| PluginName | string |  |

Queues the specified plugin to be unloaded. To avoid deadlocks, the unloading happens in the main tick thread asynchronously.

## Constants

| Name | Notes |
| --- | --- |
| HOOK_BLOCK_SPREAD | Called when a block spreads based on world conditions |
| HOOK_BLOCK_TO_PICKUPS | Called when a block has been dug and is being converted to pickups. The server has provided the default pickups and the plugins may modify them. |
| HOOK_BREWING_COMPLETED | Called when a brewing stand completed a brewing process. |
| HOOK_BREWING_COMPLETING | Called before a brewing stand completes a brewing process. |
| HOOK_CHAT | Called when a client sends a chat message that is not a command. The plugin may modify the chat message |
| HOOK_CHUNK_AVAILABLE | Called when a chunk is loaded or generated and becomes available in the {{cWorld|world}}. |
| HOOK_CHUNK_GENERATED | Called after a chunk is generated. A plugin may do last modifications on the generated chunk before it is handed of to the {{cWorld|world}}. |
| HOOK_CHUNK_GENERATING | Called before a chunk is generated. A plugin may override some parts of the generation algorithm. |
| HOOK_CHUNK_UNLOADED | Called after a chunk has been unloaded from a {{cWorld|world}}. |
| HOOK_CHUNK_UNLOADING | Called before a chunk is unloaded from a {{cWorld|world}}. The chunk has already been saved. |
| HOOK_COLLECTING_PICKUP | Called when a player is about to collect a pickup. |
| HOOK_CRAFTING_NO_RECIPE | Called when a player has items in the crafting slots and the server cannot locate any recipe. Plugin may provide a recipe. |
| HOOK_DISCONNECT | Called after the player has disconnected. |
| HOOK_DROPSPENSE | Called when a {{cDropSpenserEntity|DropSpenser}} is dropspensing an {{cItem|item}}. |
| HOOK_ENTITY_ADD_EFFECT | Called when an effect is being added to an {{cEntity|entity}}. Plugin may refuse the effect. |
| HOOK_ENTITY_CHANGED_WORLD | Called after a entity has changed the world. |
| HOOK_ENTITY_CHANGING_WORLD | Called before a entity has changed the world. Plugin may disallow a entity to change the world. |
| HOOK_ENTITY_TELEPORT | Called when an {{cEntity|entity}} is being teleported. Plugin may refuse the teleportation. |
| HOOK_EXECUTE_COMMAND | Called when a client sends a chat message that is recognized as a command, before handing that command to the regular command handler. A plugin may stop the command from being handled. This hook is called even when the player doesn't have permissions for the command. |
| HOOK_EXPLODED | Called after an explosion has been processed in a {{cWorld|world}}. |
| HOOK_EXPLODING | Called before an explosion is processed in a {{cWorld|world}}. A plugin may alter the explosion parameters or cancel the explosion altogether. |
| HOOK_HANDSHAKE | Called when a Handshake packet is received from a client. |
| HOOK_HOPPER_PULLING_ITEM | Called when a hopper is pulling an item from the container above it. |
| HOOK_HOPPER_PUSHING_ITEM | Called when a hopper is pushing an item into the container it is aimed at. |
| HOOK_KILLED | Called when an entity has been killed. |
| HOOK_KILLING | Called when an entity has just been killed. A plugin may resurrect the entity by setting its health to above zero. |
| HOOK_LOGIN | Called when a Login packet is sent to the client, before the client is queued for authentication. |
| HOOK_LOGIN_FORGE | Called when a Forge client has sent its ModList to the server, during the login handshake. |
| HOOK_PLAYER_ANIMATION | Called when a client send the Animation packet. |
| HOOK_PLAYER_BREAKING_BLOCK | Called when a player is about to break a block. A plugin may cancel the event. |
| HOOK_PLAYER_BROKEN_BLOCK | Called after a player has broken a block. |
| HOOK_PLAYER_CROUCHED | Called when a player crouches. |
| HOOK_PLAYER_DESTROYED | Called when the {{cPlayer}} object is destroyed - a player has disconnected. |
| HOOK_PLAYER_EATING | Called when the player starts eating a held item. Plugins may abort the eating. |
| HOOK_PLAYER_FISHED | Called when the player reels the fishing rod back in, after the server decides the player's fishing reward and the experience to grant. |
| HOOK_PLAYER_FISHING | Called when the player reels the fishing rod back in, plugins may alter the fishing reward and the experience granted to the player. |
| HOOK_PLAYER_FOOD_LEVEL_CHANGE | Called when the player's food level is changing. Plugins may refuse the change. |
| HOOK_PLAYER_JOINED | Called when the player entity has been created. It has not yet been fully initialized. |
| HOOK_PLAYER_LEFT_CLICK | Called when the client sends the LeftClick packet. |
| HOOK_PLAYER_MOVING | Called when the player has moved and the movement is now being applied. |
| HOOK_PLAYER_OPENING_WINDOW | Called when the player is about to open a window. The plugin can return true to cancel the window opening. |
| HOOK_PLAYER_PLACED_BLOCK | Called when the player has just placed a block |
| HOOK_PLAYER_PLACING_BLOCK | Called when the player is about to place a block. A plugin may cancel the event. |
| HOOK_PLAYER_RIGHT_CLICK | Called when the client sends the RightClick packet. |
| HOOK_PLAYER_RIGHT_CLICKING_ENTITY | Called when the client sends the UseEntity packet. |
| HOOK_PLAYER_SHOOTING | Called when the player releases the mouse button to fire their bow. |
| HOOK_PLAYER_SPAWNED | Called after the player entity has been created. The entity is fully initialized and is spawning in the {{cWorld|world}}. |
| HOOK_PLAYER_TOSSING_ITEM | Called when the player is tossing the held item (keypress Q) |
| HOOK_PLAYER_USED_BLOCK | Called after the player has right-clicked a block |
| HOOK_PLAYER_USED_ITEM | Called after the player has right-clicked with a usable item in their hand. |
| HOOK_PLAYER_USING_BLOCK | Called when the player is about to use (right-click) a block |
| HOOK_PLAYER_USING_ITEM | Called when the player is about to right-click with a usable item in their hand. |
| HOOK_PLUGINS_LOADED | Called after all plugins have loaded. |
| HOOK_PLUGIN_MESSAGE | Called when a PluginMessage packet is received from a client. |
| HOOK_POST_CRAFTING | Called after a valid recipe has been chosen for the current contents of the crafting grid. Plugins may modify the recipe. |
| HOOK_PRE_CRAFTING | Called before a recipe is searched for the current contents of the crafting grid. Plugins may provide a recipe and cancel the built-in search. |
| HOOK_PROJECTILE_HIT_BLOCK | Called when a {{cProjectileEntity|projectile}} hits a block. |
| HOOK_PROJECTILE_HIT_ENTITY | Called when a {{cProjectileEntity|projectile}} hits an {{cEntity|entity}}. |
| HOOK_SERVER_PING | Called when a client pings the server from the server list. Plugins may change the favicon, server description, players online and maximum players values. |
| HOOK_SPAWNED_ENTITY | Called after an entity is spawned in a {{cWorld|world}}. The entity is already part of the world. |
| HOOK_SPAWNED_MONSTER | Called after a mob is spawned in a {{cWorld|world}}. The mob is already part of the world. |
| HOOK_SPAWNING_ENTITY | Called just before an entity is spawned in a {{cWorld|world}}. |
| HOOK_SPAWNING_MONSTER | Called just before a mob is spawned in a {{cWorld|world}}. |
| HOOK_TAKE_DAMAGE | Called when an entity is taking any kind of damage. Plugins may modify the damage value, effects, source or cancel the damage. |
| HOOK_TICK | Called when the main server thread ticks - 20 times a second. |
| HOOK_UPDATED_SIGN | Called after a {{cSignEntity|sign}} text has been updated, either by a player or by any external means. |
| HOOK_UPDATING_SIGN | Called before a {{cSignEntity|sign}} text is updated, either by a player or by any external means. |
| HOOK_WEATHER_CHANGED | Called after the weather has changed. |
| HOOK_WEATHER_CHANGING | Called just before the weather changes |
| HOOK_WORLD_STARTED | Called when a world has been started. |
| HOOK_WORLD_TICK | Called in each world's tick thread when the game logic is about to tick (20 times a second). |
| crBlocked | When a plugin stopped the command using the OnExecuteCommand hook |
| crError | When the command handler for the given command results in an error |
| crExecuted | When the command is successfully executed. |
| crNoPermission | When the player doesn't have permission to execute the given command. |
| crUnknownCommand | When the given command doesn't exist. |
| psDisabled | The plugin is not enabled in settings.ini |
| psError | The plugin is enabled in settings.ini, but it has run into an error while loading. Use {{cPlugin}}:GetLoadError() to identify the error. |
| psLoaded | The plugin is enabled and loaded. |
| psNotFound | The plugin has been loaded, but is no longer present on disk. |
| psUnloaded | The plugin is enabled in settings.ini, but it has been unloaded (by a command). |

## Constant Groups

Results that the (Force)ExecuteCommand functions return. This gives information whether the command was executed or not, and the reason.

### CommandResult

^cr.*


					These constants identify individual hooks. To register the plugin to receive notifications on hooks, use the
					cPluginManager:AddHook() function. For detailed description of each hook, see the <a href='index.html#hooks'>
					hooks reference</a>.

### PluginHook

HOOK_.*


					These constants are used to report status of individual plugins. Use {{cPlugin}}:GetStatus() to query the
					status of a plugin; use cPluginManager::ForEachPlugin() to iterate over plugins.

### ePluginStatus

ps.*
