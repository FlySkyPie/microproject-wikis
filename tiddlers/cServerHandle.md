This class provides an interface for TCP sockets listening for a connection. In order to listen, the
plugin needs to use the {{cNetwork}}:Listen() function to create the listening socket.

Note that when Lua garbage-collects this class, the listening socket is closed. Therefore the plugin
should keep it referenced in a global variable for as long as it wants the server running.

## Functions

### Close()

Closes the listening socket. No more connections will be accepted, and all current connections will be closed.

### IsListening()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if the socket is listening.
