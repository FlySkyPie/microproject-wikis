cPlugin describes a Lua plugin. Each plugin has its own cPlugin object.

## Functions

### GetDirectory()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | string |  |

<b>OBSOLETE</b>, use GetFolderName() instead!

### GetFolderName()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | string |  |

Returns the name of the folder where the plugin's files are. (APIDump)

### GetLoadError()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | string |  |

If the plugin failed to load, returns the error message for the failure.

### GetLocalDirectory()

<b>OBSOLETE</b>, use GetLocalFolder instead.

### GetLocalFolder()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | string |  |

Returns the path where the plugin's files are. (Plugins/APIDump)

### GetName()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | string |  |

Returns the name of the plugin.

### GetStatus()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| PluginStatus | cPluginManager#ePluginStatus |  |

Returns the status of the plugin (loaded, disabled, unloaded, error, not found)

### GetVersion()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the version of the plugin.

### IsLoaded()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

### SetName(PluginApiName)

| Name | Type | Notes |
| --- | --- | --- |
| PluginApiName | string |  |

Sets the API name of the Plugin that is used by {{cPluginManager}}:CallPlugin() to identify the plugin.

### SetVersion(PluginApiVersion)

| Name | Type | Notes |
| --- | --- | --- |
| PluginApiVersion | number |  |

Sets the API version of the plugin. Currently unused.
