This article will explain how to write a basic plugin. It details basic requirements for a plugin, explains how to register a hook and bind a command, and gives plugin standards details.

Let us begin. In order to begin development, we must firstly obtain a compiled copy of Cuberite, and make sure that the Core plugin is within the Plugins folder, and activated. Core handles much of the Cuberite end-user experience and gameplay will be very bland without it.

## Creating the basic template

Plugins are written in Lua. Therefore, create a new Lua file. You can create as many files as you wish, with any filename - Cuberite bungs them all together at runtime, however, let us create a file called main.lua for now. Format it like so:

```lua
PLUGIN = nil

function Initialize(Plugin)
	Plugin:SetName("NewPlugin")
	Plugin:SetVersion(1)

	-- Hooks

	PLUGIN = Plugin -- NOTE: only needed if you want OnDisable() to use GetName() or something like that

	-- Command Bindings

	LOG("Initialised version " .. Plugin:GetVersion())
	return true
end

function OnDisable()
	LOG("Shutting down...")
end
```

Now for an explanation of the basics.

- **function Initialize** is called on plugin startup. It is the place where the plugin is set up.
- **Plugin:SetName** sets the name of the plugin.
- **Plugin:SetVersion** sets the revision number of the plugin. This must be an integer.
- **LOG** logs to console a message, in this case, it prints that the plugin was initialised. This will add a prefix with the name of your plugin.
- The **PLUGIN** variable just stores this plugin's object, so GetName() can be called in OnDisable (as no Plugin parameter is passed there, contrary to Initialize). This global variable is only needed if you want to know the plugin details (name, etc.) when shutting down.
- **function OnDisable** is called when the plugin is disabled, commonly when the server is shutting down. Perform cleanup and logging here.

Be sure to return true for this function, else Cuberite thinks you plugin had failed to initialise and prints a stacktrace with an error message.

## Registering hooks

Hooks are things that Cuberite calls when an internal event occurs. For example, a hook is fired when a player places a block, moves, logs on, eats, and many other things. For a full list, see [the API documentation](index.html).

A hook can be either informative or overridable. In any case, returning false will not trigger a response, but returning true will cancel the hook and prevent it from being propagated further to other plugins. An overridable hook simply means that there is visible behaviour to a hook's cancellation, such as a chest being prevented from being opened. There are some exceptions to this where only changing the value the hook passes has an effect, and not the actual return value, an example being the HOOK_KILLING hook. See the API docs for details.

To register a hook, insert the following code template into the "-- Hooks" area in the previous code example.

```lua
cPluginManager.AddHook(cPluginManager.HOOK_NAME_HERE, FunctionNameToBeCalled)
```

What does this code do?

- **cPluginManager.AddHook** registers the hook. The hook name is the second parameter. See the previous API documentation link for a list of all hooks.

What about the third parameter, you ask? Well, it is the name of the function that Cuberite calls when the hook fires. It is in this function that you should handle or cancel the hook.

So in total, this is a working representation of what we have so far covered.

```lua
function Initialize(Plugin)
	Plugin:SetName("DerpyPlugin")
	Plugin:SetVersion(1)

	cPluginManager.AddHook(cPluginManager.HOOK_PLAYER_MOVING, OnPlayerMoving)

	LOG("Initialised " .. Plugin:GetName() .. " v." .. Plugin:GetVersion())
	return true
end

function OnPlayerMoving(Player) -- See API docs for parameters of all hooks
	return true -- Prohibit player movement, see docs for whether a hook is cancellable
end
```

So, that code stops the player from moving. Not particularly helpful, but yes :P. Note that ALL documentation is available on the main API docs page, so if ever in doubt, go there.

## Binding a command

### Format

So now we know how to hook into Cuberite, how do we bind a command, such as /explode, for a player to type? That is more complicated. We firstly add this template to the "-- Command bindings" section of the initial example:

```lua
-- ADD THIS IF COMMAND DOES NOT REQUIRE A PARAMETER (/explode)
cPluginManager.BindCommand("/commandname", "permissionnode", FunctionToCall, " - Description of command")

-- ADD THIS IF COMMAND DOES REQUIRE A PARAMETER (/explode Notch)
cPluginManager.BindCommand("/commandname", "permissionnode", FunctionToCall, " ~ Description of command and parameter(s)")
```

What does it do, and why are there two?

- **PluginManager:BindCommand** binds a command. It takes the command name (with a slash), the permission a player needs to execute the command, the function to call when the command is executed, and a description of the command.

The command name is pretty self explanatory. The permission node is basically just a **string** that the player's group needs to have, so you can have anything in there, though we recommend a style such as "derpyplugin.explode". The function to call is like the ones with Hooks, but with some fixed parameters which we will come on to later, and the description is a description of the command which is shown when "/help" is typed.

So why are there two? Standards. A plugin that accepts a parameter MUST use a format for the description of " ~ Description of command and parms" whereas a command that doesn't accept parameters MUST use " - Description of command" instead. Be sure to put a space before the tildes or dashes. Additionally, try to keep the description brief and on one line on the client.

### Parameters

What parameters are in the function Cuberite calls when the command is executed? A 'Split' array and a 'Player' object.

#### The Split Array

The Split array is an array of all text submitted to the server, including the actual command. Cuberite automatically splits the text into the array, so plugin authors do not need to worry about that. An example of a Split array passed for the command, "/derp zubby explode" would be:

```
/derp (Split[1])
zubby (Split[2])
explode (Split[3])

The total amount of parameters passed were: 3 (#Split)
```

#### The Player Object and sending them messages

The Player object is basically a pointer to the player that has executed the command. You can do things with them, but most common is sending a message. Again, see the API documentation for fuller details. But, you ask, how *do* we send a message to the client?

There are dedicated functions used for sending a player formatted messages. By format, I refer to coloured prefixes/coloured text (depending on configuration) that clearly categorise what type of message a player is being sent. For example, an informational message has a yellow coloured [INFO] prefix, and a warning message has a rose coloured [WARNING] prefix. A few of the most used functions are listed here, but see the API docs for more details. Look in the cRoot, cWorld, and cPlayer sections for functions that broadcast to the entire server, the whole world, and a single player, respectively.

```lua
-- Format: §yellow[INFO] §white%text% (yellow [INFO], white text following it)
-- Use: Informational message, such as instructions for usage of a command
Player:SendMessageInfo("Usage: /explode [player]")

-- Format: §green[INFO] §white%text% (green [INFO] etc.)
-- Use: Success message, like when a command executes successfully
Player:SendMessageSuccess("Notch was blown up!")

-- Format: §rose[INFO] §white%text% (rose coloured [INFO] etc.)
-- Use: Failure message, like when a command was entered correctly but failed to run, such as when the destination player wasn't found in a /tp command
Player:SendMessageFailure("Player Salted was not found")
```

Those are the basics. If you want to output text to the player for a reason other than the three listed above, and you want to colour the text, simply concatenate "cChatColor.*colorhere*" with your desired text, concatenate being "..". See the API docs for more details of all colours, as well as details on logging to console with LOG("Text").

## Final example and conclusion

So, a working example that checks the validity of a command, and blows up a player, and also refuses pickup collection to players with >100ms ping.

```lua
function Initialize(Plugin)
	Plugin:SetName("DerpyPluginThatBlowsPeopleUp")
	Plugin:SetVersion(9001)

	cPluginManager.BindCommand("/explode", "derpyplugin.explode", Explode, " ~ Explode a player");

	cPluginManager:AddHook(cPluginManager.HOOK_COLLECTING_PICKUP, OnCollectingPickup)

	LOG("Initialised " .. Plugin:GetName() .. " v." .. Plugin:GetVersion())
	return true
end

function OnCollectingPickup(Player, Pickup)
	-- Check the player's ping
	if (Player:GetClientHandle():GetPing() > 100) then
		return true -- Do not let the player collect the pickup
	end
	return false -- Allow the player to collect the pickup
end

function Explode(Split, Player)
	if (Split[2] == nil) then
		-- No player name was given. Error!
		Player:SendMessageFailure("Please use '/explode <player>'")
		return true
	end

	-- Attempt to find the player named.
	local ExplodePlayer = Player:GetWorld():FindPlayer(Split[2])
	if (ExplodePlayer == nil) then
		-- Player not found!
		Player:SendMessageFailure("Player \"" .. Split[2] .. "\" not found")
		return true
	end

	-- Actual explosion
	local World = Player:GetWorld()
	World:DoExplosionAt(10, ExplodePlayer:GetPosX(), ExplodePlayer:GetPosY(), ExplodePlayer:GetPosZ(), false, nil)
	Player:SendMessageSuccess("Player \"" .. ExplodePlayer:GetName() .. "\" has been blown up!")
	return true
end
```

That sums it all up. The approach towards writing a Cuberite plugin is not the hardest thing. It all depends on what you want to do with it - and this is a massive learning curve. But you've just completed the first step, good luck!