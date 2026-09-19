Represents a UDP socket that is listening for incoming datagrams on a UDP port and can send or broadcast datagrams to other peers on the network. Plugins can create an instance of the endpoint by calling {{cNetwork}}:CreateUDPEndpoint(). The endpoints are callback-based - when a datagram is read from the network, the OnRececeivedData() callback is called with details about the datagram. See the additional information in {{cNetwork}} documentation for details.

Note that when Lua garbage-collects this class, the listening socket is closed. Therefore the plugin should keep this object referenced in a global variable for as long as it wants the endpoint open.

## Functions

### Close()

Closes the UDP endpoint. No more datagrams will be reported through the callbacks, the UDP port will be closed.

### EnableBroadcasts()

Some OSes need this call before they allow UDP broadcasts on an endpoint.

### GetPort()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the local port number of the UDP endpoint listening for incoming datagrams. Especially useful if the UDP endpoint was created with auto-assign port (0).

### IsOpen()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Returns true if the UDP endpoint is listening for incoming datagrams.

### Send(RawData, RemoteHost, RemotePort)

| Name | Type | Notes |
| --- | --- | --- |
| RawData | string |  |
| RemoteHost | string |  |
| RemotePort | number |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | boolean |  |

Sends the specified raw data (string) to the specified remote host. The RemoteHost can be either a hostname or an IP address; if it is a hostname, the endpoint will queue a DNS lookup first, if it is an IP address, the send operation is executed immediately. Returns true if there was no immediate error, false on any failure. Note that the return value needn't represent whether the packet was actually sent, only if it was successfully queued.
