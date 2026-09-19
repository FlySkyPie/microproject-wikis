This class encapsulates all the data that is sent to the WebAdmin through one HTTP request. Plugins
receive this class as a parameter to the function handling the web requests, as registered in the
{{cPluginLua}}:AddWebPage().

## Constants

| Name | Notes |
| --- | --- |
| FormData | Array-table of {{HTTPFormData}}, contains the values of individual form elements submitted by the client |
| Params | Map-table of parameters given to the request in the URL (?param=value); if a form uses GET method, this is the same as FormData. For each parameter given as "param=value", there is an entry in the table with "param" as its key and "value" as its value. |
| PostParams | Map-table of data posted through a FORM - either a GET or POST method. Logically the same as FormData, but in a map-table format (for each parameter given as "param=value", there is an entry in the table with "param" as its key and "value" as its value). |

## Variables

| Name | Type | Notes |
| --- | --- | --- |
| Method | string | The HTTP method used to make the request. Usually GET or POST. |
| Path | string | The Path part of the URL (excluding the parameters) |
| URL | string | The entire URL used for the request. |
| Username | string | Name of the logged-in user. |
