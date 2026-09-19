This is the namespace for high-level network-related operations. Allows plugins to make TCP
connections to the outside world using a callback-based API.

All functions in this namespace are static, they should be called on the cNetwork class itself:

```
local Server = cNetwork:Listen(1024, ListenCallbacks);
```

## Functions

### **Static** Connect(Host, Port, LinkCallbacks)

| Name | Type | Notes |
| --- | --- | --- |
| Host | string |  |
| Port | number |  |
| LinkCallbacks | table |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Begins establishing a (client) TCP connection to the specified host. Uses the LinkCallbacks table to report progress, success, errors and incoming data. Returns false if it fails immediately (bad port value, bad hostname format), true otherwise. Host can be either an IP address or a hostname.

### **Static** CreateUDPEndpoint(Port, UDPCallbacks)

| Name | Type | Notes |
| --- | --- | --- |
| Port | number |  |
| UDPCallbacks | table |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | cUDPEndpoint |  |

Creates a UDP endpoint that listens for incoming datagrams on the specified port, and can be used to send or broadcast datagrams. Uses the UDPCallbacks to report incoming datagrams or errors. If the endpoint cannot be created, the OnError callback is called with the error details and the returned endpoint will report IsOpen() == false. The plugin needs to store the returned endpoint object for as long as it needs the UDP port open; if the endpoint is garbage-collected by Lua, the socket will be closed and no more incoming data will be reported.<br>If the Port is zero, the OS chooses an available UDP port for the endpoint; use {{cUDPEndpoint}}:GetPort() to query the port number in such case.

### **Static** EnumLocalIPAddresses()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | table |  |

Returns all local IP addresses for network interfaces currently available on the machine, as an array-table of strings.

### **Static** HostnameToIP(Host, LookupCallbacks)

| Name | Type | Notes |
| --- | --- | --- |
| Host | string |  |
| LookupCallbacks | table |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Begins a DNS lookup to find the IP address(es) for the specified host. Uses the LookupCallbacks table to report progress, success or errors. Returns false if it fails immediately (bad hostname format), true if the lookup started successfully. Host can be either a hostname or an IP address.

### **Static** IPToHostname(Address, LookupCallbacks)

| Name | Type | Notes |
| --- | --- | --- |
| Address | string |  |
| LookupCallbacks | table |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Begins a reverse-DNS lookup to find out the hostname for the specified IP address. Uses the LookupCallbacks table to report progress, success or errors. Returns false if it fails immediately (bad address format), true if the lookup started successfully.

### **Static** Listen(Port, ListenCallbacks)

| Name | Type | Notes |
| --- | --- | --- |
| Port | number |  |
| ListenCallbacks | table |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | cServerHandle |  |

Starts listening on the specified port. Uses the ListenCallbacks to report incoming connections or errors. Returns a {{cServerHandle}} object representing the server. If the listen operation failed, the OnError callback is called with the error details and the returned server handle will report IsListening() == false. The plugin needs to store the server handle object for as long as it needs the server running, if the server handle is garbage-collected by Lua, the listening socket will be closed and all current connections dropped.

## Additional Info

### Using callbacks

The entire Networking API is callback-based. Whenever an event happens on the network object, a
specific plugin-provided function is called. The callbacks are stored in tables which are passed
to the API functions, each table contains multiple callbacks for the various situations.

There are four different callback variants used: LinkCallbacks, LookupCallbacks, ListenCallbacks
and UDPCallbacks. Each is used in the situation appropriate by its name - LinkCallbacks are used
for handling the traffic on a single network link (plus additionally creation of such link when
connecting as a client), LookupCallbacks are used when doing DNS and reverse-DNS lookups,
ListenCallbacks are used for handling incoming connections as a server and UDPCallbacks are used
for incoming UDP datagrams.

LinkCallbacks have the following structure:

```
local LinkCallbacks =
{
	OnConnected = function ({{cTCPLink|a_TCPLink}})
		-- The specified {{cTCPLink|link}} has succeeded in connecting to the remote server.
		-- Only called if the link is being connected as a client (using cNetwork:Connect() )
		-- Not used for incoming server links
		-- All returned values are ignored
	end,

	OnError = function ({{cTCPLink|a_TCPLink}}, a_ErrorCode, a_ErrorMsg)
		-- The specified error has occured on the {{cTCPLink|link}}
		-- No other callback will be called for this link from now on
		-- For a client link being connected, this reports a connection error (destination unreachable etc.)
		-- It is an Undefined Behavior to send data to a_TCPLink in or after this callback
		-- All returned values are ignored
	end,

	OnReceivedData = function ({{cTCPLink|a_TCPLink}}, a_Data)
		-- Data has been received on the {{cTCPLink|link}}
		-- Will get called whenever there's new data on the {{cTCPLink|link}}
		-- a_Data contains the raw received data, as a string
		-- All returned values are ignored
	end,

	OnRemoteClosed = function ({{cTCPLink|a_TCPLink}})
		-- The remote peer has closed the {{cTCPLink|link}}
		-- The link is already closed, any data sent to it now will be lost
		-- No other callback will be called for this link from now on
		-- All returned values are ignored
	end,
}
```

LookupCallbacks have the following structure:

```
local LookupCallbacks =
{
	OnError = function (a_Query, a_ErrorCode, a_ErrorMsg)
		-- The specified error has occured while doing the lookup
		-- a_Query is the hostname or IP being looked up
		-- No other callback will be called for this lookup from now on
		-- All returned values are ignored
	end,

	OnFinished = function (a_Query)
		-- There are no more DNS records for this query
		-- a_Query is the hostname or IP being looked up
		-- No other callback will be called for this lookup from now on
		-- All returned values are ignored
	end,

	OnNameResolved = function (a_Hostname, a_IP)
		-- A DNS record has been found, the specified hostname resolves to the IP
		-- Called for both Hostname -> IP and IP -> Hostname lookups
		-- May be called multiple times if a hostname resolves to multiple IPs
		-- All returned values are ignored
	end,
}
```

ListenCallbacks have the following structure:

```
local ListenCallbacks =
{
	OnAccepted = function ({{cTCPLink|a_TCPLink}})
		-- A new connection has been accepted and a {{cTCPLink|Link}} for it created
		-- It is safe to send data to the link now
		-- All returned values are ignored
	end,

	OnError = function (a_ErrorCode, a_ErrorMsg)
		-- The specified error has occured while trying to listen
		-- No other callback will be called for this server handle from now on
		-- This callback is called before the cNetwork:Listen() call returns
		-- All returned values are ignored
	end,

	OnIncomingConnection = function (a_RemoteIP, a_RemotePort, a_LocalPort)
		-- A new connection is being accepted, from the specified remote peer
		-- This function needs to return either nil to drop the connection,
		-- or valid LinkCallbacks to use for the new connection's {{cTCPLink|TCPLink}} object
		return SomeLinkCallbacks
	end,
}
```

UDPCallbacks have the following structure:

```
local UDPCallbacks =
{
	OnError = function (a_ErrorCode, a_ErrorMsg)
		-- The specified error has occured when trying to listen for incoming UDP datagrams
		-- No other callback will be called for this endpoint from now on
		-- This callback is called before the cNetwork:CreateUDPEndpoint() call returns
		-- All returned values are ignored
	end,

	OnReceivedData = function ({{cUDPEndpoint|a_UDPEndpoint}}, a_Data, a_RemotePeer, a_RemotePort)
		-- A datagram has been received on the {{cUDPEndpoint|endpoint}} from the specified remote peer
		-- a_Data contains the raw received data, as a string
		-- All returned values are ignored
	end,
}
```

### Example client connection

The following example, adapted from the NetworkTest plugin, shows a simple example of a client
connection using the cNetwork API. It connects to www.google.com on port 80 (http) and sends a http
request for the front page. It dumps the received data to the console.

First, the callbacks are defined in a table. The OnConnected() callback takes care of sending the http
request once the socket is connected. The OnReceivedData() callback sends all data to the console. The
OnError() callback logs any errors. Then, the connection is initiated using the cNetwork::Connect() API
function.

```
-- Define the callbacks to use for the client connection:
local ConnectCallbacks =
{
	OnConnected = function (a_Link)
		-- Connection succeeded, send the http request:
		a_Link:Send("GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n")
	end,

	OnError = function (a_Link, a_ErrorCode, a_ErrorMsg)
		-- Log the error to console:
		LOG("An error has occurred while talking to google.com: " .. a_ErrorCode .. " (" .. a_ErrorMsg .. ")")
	end,

	OnReceivedData = function (a_Link, a_Data)
		-- Log the received data to console:
		LOG("Incoming http data:\r\n" .. a_Data)
	end,

	OnRemoteClosed = function (a_Link)
		-- Log the event into the console:
		LOG("Connection to www.google.com closed")
	end,
}

-- Connect:
if not(cNetwork:Connect("www.google.com", 80, ConnectCallbacks)) then
	-- Highly unlikely, but better check for errors
	LOG("Cannot queue connection to www.google.com")
end
-- Note that the connection is being made on the background,
-- there's no guarantee that it's already connected at this point in code
```

### Example server implementation

The following example, adapted from the NetworkTest plugin, shows a simple example of creating a
server listening on a TCP port using the cNetwork API. The server listens on port 9876 and for
each incoming connection it sends a welcome message and then echoes back whatever the client has
sent ("echo server").

First, the callbacks for the listening server are defined. The most important of those is the
OnIncomingConnection() callback that must return the LinkCallbacks that will be used for the new
connection. In our simple scenario each connection uses the same callbacks, so a predefined
callbacks table is returned; it is, however, possible to define different callbacks for each
connection. This allows the callbacks to be "personalised", for example by the remote IP or the
time of connection. The OnAccepted() and OnError() callbacks only log that they occurred, there's
no processing needed for them.

Finally, the cNetwork:Listen() API function is used to create the listening server. The status of
the server is checked and if it is successfully listening, it is stored in a global variable, so
that Lua doesn't garbage-collect it until we actually want the server closed.

```
-- Define the callbacks used for the incoming connections:
local EchoLinkCallbacks =
{
	OnConnected = function (a_Link)
		-- This will not be called for a server connection, ever
		assert(false, "Unexpected Connect callback call")
	end,

	OnError = function (a_Link, a_ErrorCode, a_ErrorMsg)
		-- Log the error to console:
		local RemoteName = "'" .. a_Link:GetRemoteIP() .. ":" .. a_Link:GetRemotePort() .. "'"
		LOG("An error has occurred while talking to " .. RemoteName .. ": " .. a_ErrorCode .. " (" .. a_ErrorMsg .. ")")
	end,

	OnReceivedData = function (a_Link, a_Data)
		-- Send the received data back to the remote peer
		a_Link:Send(Data)
	end,

	OnRemoteClosed = function (a_Link)
		-- Log the event into the console:
		local RemoteName = "'" .. a_Link:GetRemoteIP() .. ":" .. a_Link:GetRemotePort() .. "'"
		LOG("Connection to '" .. RemoteName .. "' closed")
	end,
}

-- Define the callbacks used by the server:
local ListenCallbacks =
{
	OnAccepted = function (a_Link)
		-- No processing needed, just log that this happened:
		LOG("OnAccepted callback called")
	end,

	OnError = function (a_ErrorCode, a_ErrorMsg)
		-- An error has occured while listening for incoming connections, log it:
		LOG("Cannot listen, error " .. a_ErrorCode .. " (" .. a_ErrorMsg .. ")"
	end,

	OnIncomingConnection = function (a_RemoteIP, a_RemotePort, a_LocalPort)
		-- A new connection is being accepted, give it the EchoCallbacks
		return EchoLinkCallbacks
	end,
}

-- Start the server:
local Server = cNetwork:Listen(9876, ListenCallbacks)
if not(Server:IsListening()) then
	-- The error has been already printed in the OnError() callbacks
	-- Just bail out
	return;
end

-- Store the server globally, so that it stays open:
g_Server = Server

...

-- Elsewhere in the code, when terminating:
-- Close the server and let it be garbage-collected:
g_Server:Close()
g_Server = nil
```
