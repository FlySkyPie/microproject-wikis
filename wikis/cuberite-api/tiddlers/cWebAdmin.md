## Functions

### **Static** AddWebTab(Title, UrlPath, HandlerFn)

| Name | Type | Notes |
| --- | --- | --- |
| Title | string |  |
| UrlPath | string |  |
| HandlerFn | function |  |

Adds a new web tab to webadmin. The tab uses "Title" as its display string and is identified in the URL using the UrlPath (https://server.domain.com/webadmin/{PluginName}/{UrlPath}). The HandlerFn is the callback function that is called when the admin accesses the page, it has the following signature:<br/><pre class="prettyprint lang-lua">function ({{HTTPRequest|a_Request}}, a_UrlPath)<br/>  return Content, ContentType<br/>end</pre> URLPath must not contain a '/', the recommendation is to use only 7-bit-clean ASCII character set.

### **Static** GetAllWebTabs()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | table |  |

Returns an array-table with each item describing a web tab, for all web tabs registered in the WebAdmin, for all plugins. The returned table has the following format:<br/><pre class="prettyprint lang-lua">{<br/>  {<br/>    PluginName = "Plugin's API name",<br/>    UrlPath = "UrlPath given to AddWebTab",<br/>    Title = "Title given to AddWebTab",<br/>  },<br/>  ...<br/>}

### **Static** GetBaseURL(URL)

| Name | Type | Notes |
| --- | --- | --- |
| URL | string |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | string |  |

Returns the string that is the path of the base webadmin ("../../../webadmin") relative to the given URL.

### **Static** GetContentTypeFromFileExt(FileExt)

| Name | Type | Notes |
| --- | --- | --- |
| FileExt | string |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | string |  |

Returns the content-type that should be used for files with the specified extension (without the dot), such as "text/plain" for the "txt" extension. If the extension is not known, returns an empty string.

### **Static** GetHTMLEscapedString(Input)

| Name | Type | Notes |
| --- | --- | --- |
| Input | string |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | string |  |

Gets the HTML-escaped representation of a requested string. This is useful for user input and game data that is not guaranteed to be escaped already.

### **Static** GetPage(Request)

| Name | Type | Notes |
| --- | --- | --- |
| Request | HTTPRequest |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | table |  |

Returns the (inner HTML) page contents for the specified request. Calls the appropriate WebTab handler registered via AddWebTab() and returns the information from that plugin wrapped in a table with the following structure:<br/><pre class="prettyprint lang-lua">{<br/>  Content = "",      -- Content returned by the plugin<br/>  ContentType = "",  -- Content type returned by the plugin, or "text/html" if none returned<br/>  UrlPath = "",      -- UrlPath decoded from the request<br/>  TabTitle = "",     -- Title of the tab that handled the request, as given to AddWebTab()<br/>  PluginName = "",   -- API name of the plugin that handled the request<br/>  PluginFolder = "", -- Folder name (= display name) of the plugin that handled the request<br/>}</pre>This function is mainly used in the webadmin template file.

### GetPorts()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | string |  |

Returns a comma-separated list of ports on which the webadmin is configured to listen. Note that this list does include ports that may currently be unavailable (another server was already listening on them prior to launching Cuberite).

### **Static** GetURLEncodedString(Input)

| Name | Type | Notes |
| --- | --- | --- |
| Input | string |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | string |  |

<b>OBSOLETE</b> - use {{cUrlParser}}:UrlEncode() instead.<br/>Returns the string given to it escaped by URL encoding, which makes the string suitable for transmission in an URL. Invalid characters are turned into "%xy" values.

### Reload()

Reloads the webadmin's config - the allowed logins, the template script and the login page. Note that reloading will not change the "enabled" state of the server, and it will not update listening ports. Existing WebTabs will be kept registered even after the reload.
