## Contents

- [Introduction](#introduction)
- [The overall structure](#the-overall-structure)
- [AdditionalInfo table](#additionalinfo-table)
- [Commands table](#commands-table)
- [ConsoleCommands table](#consolecommands-table)
- [Permissions table](#permissions-table)
- [Categories table](#categories-table)
- [Using the file in code](#using-the-file-in-code)
- [Examples](#examples)

---

## Introduction

For a long time Cuberite plugins were plagued by poor documentation. The plugins worked, people who wrote them knew how to use them, but for anyone new to the plugin it was a terrible ordeal learning how to use it. Most of the times, the plugin authors only wrote what commands the plugin supported, sometimes not even that. Then, there was a call to action to put an end to this, to make documenting the plugins easy and at the same time centralized. Thus, the Info.lua file was born.

Most plugins have some parts that are the same across all the plugins. These are commands, console commands and their permissions. If a plugin implemented a command, it would practically copy & paste the same code over and over again. So it makes sense to extract only unique information, centralize it and automate all the parts around it. This was another reason for the Info.lua file - it is a central hub of commands, console commands and their permissions.

Last, but not least, we want to make a plugin repository on the web in the future, a repository that would store plugins, their descriptions, comments. It makes sense that the centralized information can be parsed by the repository automatically, so that advanced things, such as searching for a plugin based on a command, or determining whether two plugins collide command-wise, are possible.

A tool has been written that allows for an easy generation of the documentation for the plugin in various formats. It outputs the documentation in a format that is perfect for pasting into the forum. It generates documentation in a Markup format to use in README.md on GitHub and similar sites. The clever thing is that you don't need to keep all those formats in sync manually - you edit the Info.lua file and this tool will re-generate the documentation for you.

To generate documentation for the plugin, activate the DumpInfo plugin on a cuberite server with your plugin installed, and use the webadmin interface to "Dump" the plugin information. This will create a README.md suitable for uploading to your git repo, and a forum_info.txt, which can be copy-pasted into a forum post.

So to sum up, the Info.lua file contains the plugins' commands, console commands, their permissions and possibly the overall plugin documentation, in a structured manner that can be parsed by a program, yet is human readable and editable.

---

## The overall structure

The file consist of a declaration of a single Lua table, g_PluginInfo. This table contains all the information, structured, as its members. Each member can be a structure by itself. The entire file is a valid Lua source file, so any tool that syntax-checks Lua source can syntax-check this file. The file is somewhat forward- and backward- compatible, in the sense that it can be extended in any way without breaking.

Here's a skeleton of the file:

```lua
g_PluginInfo =
{
	Name = "Example Plugin",
	Date = "2014-06-12",
	Description = "This is an example plugin that shows how to use the Info.lua file",

	-- The following members will be documented in greater detail later:
	AdditionalInfo = {},
	Commands = {},
	ConsoleCommands = {},
	Permissions = {},
	Categories = {},
}
```

As you can see, the structure is pretty straightforward. Note that the order of the elements inside the table is not important (Lua property).

The first few elements are for book-keeping. They declare the plugin's name, the date in ISO-format, representing the version of the plugin, and the description. The idea is that the description sums up what the plugin is all about, within some two or three sentences.

---

## AdditionalInfo table

This table is used for more detailed description of the plugin. If there is any non-trivial setup process, dependencies, describe them here. This is where the description should get detailed. Don't worry about using several paragraphs of text here, if it makes the plugin easier to understand.

The table should have the following layout:

```lua
AdditionalInfo =
{
	{
		Title = "Chapter 1",
		Contents = "Describe one big aspect of the plugin here",
	},
	{
		Title = "Chapter 2",
		Contents = "Describe another big topic",
	},
}
```

The idea here is that the tool that is used to generate the documentation from the Info.lua file will create a linkified table of contents and then each of the information elements' contents. This information should be all that is needed to successfully configure, run and manage the plugin.

---

## Commands table

The commands table lists all the commands that the plugin implements, together with their handler functions, required permissions, help strings and further information. The table supports recursion, which allows plugins to create multi-word commands easily (such as "//schematic load" and "//schematic save"), each having its own separate handler.

The table uses structure similar to the following:

```lua
Commands =
{
	["/cmd1"] =
	{
		HelpString = "Performs the first action",
		Permission = "firstplugin.cmds.1",
		Alias = "/c1",
		Handler = HandleCmd1,
		ParameterCombinations =
		{
			{
				Params = "x y z",
				Help = "Performs the first action at the specified coordinates",
			},
			{
				Params = "-p",
				Help = "Performs the first action at the player's coordinates",
			}
		},
	},
	["/cmd2"] =
	{
		Alias = {"/c2", "//c2" },
		Category = "Something",
		Subcommands =
		{
			sub1 =  -- This declares a "/cmd2 sub1" command
			{
				HelpString = "Performs the second action's first subcommand",
				Permission = "firstplugin.cmds.2.1",
				Alias = "1",
				Handler = HandleCmd2Sub1,
				ParameterCombinations =
				{
					{
						Params = "x y z",
						Help = "Performs the second action's first subcommand at the specified coordinates",
					},
					{
						Params = "-p",
						Help = "Performs the second action's first subcommand at the player's coordinates",
					}
				},
			},
			sub2 =  -- Declares a "/cmd2 sub2" command
			{
				HelpString = "Performs the second action's second subcommand",
				Permission = "firstplugin.cmds.2.2",
				Handler = HandleCmd2Sub2,
			},
		},
	},
}
```

Although it may seem overwhelming at first, there is a "method to this madness". Each element of the Commands table defines one command. Most commands start with a slash, so the special Lua syntax for table elements with non-standard names needs to be applied (`["/cmd1"] =`). The command can either specify subcommands, or a handler function (specifying both is UndefinedBehavior). Subcommands uses the same structure as the entire Commands table, recursively.

The permission element specifies that the command is only available with the specified permission. Note that the permission for subcommand's parent isn't checked when the subcommand is called. This means that specifying the permission for a command that has subcommands has no effect whatsoever, but is discouraged because we may add processing for that in the future.

The optional Categories table provides descriptions for command categories in the generated documentation. The documentation generator will group the commands by their specified Category ("General" by default) and each category will have the specified description written to it.

The ParameterCombinations table is used only for generating the documentation, it lists the various combinations of parameters that the command supports. It's worth specifying even if the command supports only one combination, because that combination will get documented this way.

The Alias member specifies any possible aliases for the command. Each alias is registered separately and if there is a subcommand table, it is applied to all aliases, just as one would expect. You can specify either a single string as the value (if there's only one alias), or a table of strings for multiple aliases. Commands with no aliases do not need to specify this member at all.

---

## ConsoleCommands table

This table serves a purpose similar to that of the Commands table, only these commands are provided for the server console. Therefore, there are no permissions specified for these commands. Since most console commands don't use a leading slash, the command names don't need the special syntax. Also, the handler function doesn't receive the Player parameter.

Here's an example of a ConsoleCommands table:

```lua
ConsoleCommands =
{
	concmd =
	{
		HelpString = "Performs the console action",
		Subcommands =
		{
			sub1 =
			{
				HelpString = "Performs the console action's first subcommand",
				Handler = HandleConCmdSub1,
				ParameterCombinations =
				{
					{
						Params = "x y z",
						Help = "Performs the console action's first subcommand at the specified coordinates",
					},
				},
			},
			sub2 =
			{
				HelpString = "Performs the console action's second subcommand",
				Handler = HandleConCmdSub2,
			},
		},
	},
}
```

---

## Permissions table

The purpose of this table is to document permissions that the plugin uses. The documentation generator automatically collects the permissions specified in the Command table; the Permissions table adds a description for these permissions and may declare other permissions that aren't specifically included in the Command table.

```lua
Permissions =
{
	["firstplugin.cmd.1.1"] =
	{
		Description = "Allows the players to build high towers using the first action.",
		RecommendedGroups = "players",
	},
	["firstplugin.cmd.2.1"] =
	{
		Description = "Allows the players to kill entities using the second action. Note that this may be misused to kill other players, too.",
		RecommendedGroups = "admins, mods",
	},
}
```

The RecommendedGroup element lists, in plain English, the intended groups for which the permission should be enabled on a typical server. Plugin authors are advised to create reasonable defaults, prefering security to openness, so that admins using these settings blindly don't expose their servers to malicious users.

---

## Categories

The optional Categories table provides descriptions for categories in the generated documentation. Commands can have categories with or without category descriptions in this table. The documentation generator will output a table of listed categories along with their description.

```lua
Categories = 
{
	General =
	{
		Description = "A general, yet somehow vague description of the default category."
	},
	Something =
	{
		Description = "Some descriptive words which form sentences pertaining to this set of commands use and goals."
	},
},
```

---

## Using the file in code

Just writing the Info.lua file and saving it to the plugin folder is not enough for it to actually be used. Your plugin needs to include the following boilerplate code, preferably in its Initialize() function:

```lua
-- Use the InfoReg shared library to process the Info.lua file:
dofile(cPluginManager:GetPluginsPath() .. "/InfoReg.lua")
RegisterPluginInfoCommands()
RegisterPluginInfoConsoleCommands()
```

Of course, if your plugin doesn't have any console commands, it doesn't need to call the RegisterPluginInfoConsoleCommands() function, and similarly if it doesn't have any in-game commands, it doesn't need to call the RegisterPluginInfoCommands() function.

---

## Examples

There are several plugins that already implement this approach. You can visit them for inspiration and to see what the generated documentation looks like:

- Gallery plugin: [Info.lua](https://github.com/cuberite/gallery/blob/master/Info.lua), [Forum](https://forum.cuberite.org/thread-1306.html) documentation
- WorldEdit plugin: [Info.lua](https://github.com/cuberite/WorldEdit/blob/master/Info.lua), [Forum](https://forum.cuberite.org/thread-870.html) and [MarkDown](https://github.com/cuberite/WorldEdit) documentation