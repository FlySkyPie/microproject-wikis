This class wraps a single TCP connection, that has been established. Plugins can create these by
calling {{cNetwork}}:Connect() to connect to a remote server, or by listening using
{{cNetwork}}:Listen() and accepting incoming connections. The links are callback-based - when an event
such as incoming data or remote disconnect happens on the link, a specific callback is called. See the
additional information in {{cNetwork}} documentation for details.

The link can also optionally perform TLS encryption. Plugins can use the StartTLSClient() function to
start the TLS handshake as the client side. Since that call, the OnReceivedData() callback is
overridden internally so that the data is first routed through the TLS decryptor, and the plugin's
callback is only called for the decrypted data, once it starts arriving. The Send function changes its
behavior so that the data written by the plugin is first encrypted and only then sent over the
network. Note that calling Send() before the TLS handshake finishes is supported, but the data is
queued internally and only sent once the TLS handshake is completed.

## Functions

### Close()

Closes the link forcefully (TCP RST). There's no guarantee that the last sent data is even being delivered. See also the Shutdown() method.

### GetLocalIP()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | string |  |

Returns the IP address of the local endpoint of the TCP connection.

### GetLocalPort()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the port of the local endpoint of the TCP connection.

### GetRemoteIP()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | string |  |

Returns the IP address of the remote endpoint of the TCP connection.

### GetRemotePort()

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
|  | number |  |

Returns the port of the remote endpoint of the TCP connection.

### Send(Data)

| Name | Type | Notes |
| --- | --- | --- |
| Data | string |  |

Sends the data (raw string) to the remote peer. The data is sent asynchronously and there is no report on the success of the send operation, other than the connection being closed or reset by the underlying OS.

### Shutdown()

Shuts the socket down for sending data. Notifies the remote peer that there will be no more data coming from us (TCP FIN). The data that is in flight will still be delivered. The underlying socket will be closed when the remote end shuts down as well, or after a timeout.

### StartTLSClient(OwnCert, OwnPrivateKey, OwnPrivateKeyPassword, TrustedRootCAs)

| Name | Type | Notes |
| --- | --- | --- |
| OwnCert | string |  |
| OwnPrivateKey | string |  |
| OwnPrivateKeyPassword | string |  |
| TrustedRootCAs | string |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| IsSuccess | boolean |  |
| ErrorMessage | string |  |

Starts a TLS handshake on the link, as a client side of the TLS. The Own___ parameters specify the client certificate and its corresponding private key and password; all three parameters are optional and no client certificate is presented to the remote peer if they are not used or all empty. Once the TLS handshake is started by this call, all incoming data is first decrypted before being sent to the OnReceivedData callback, and all outgoing data is queued until the TLS handshake completes, and then sent encrypted over the link. Returns true on success, nil and optional error message on immediate failure.<br/>The TrustedRootCAs is a string containing all certificates that should be trusted, in PEM format, concatenated and separated by a newline.<b>NOTE:</b> If TrustedRootCAs is empty or nil, the server's certificate will NOT be verified, which is UNSAFE!

### StartTLSServer(Certificate, PrivateKey, PrivateKeyPassword, StartTLSData)

| Name | Type | Notes |
| --- | --- | --- |
| Certificate | string |  |
| PrivateKey | string |  |
| PrivateKeyPassword | string |  |
| StartTLSData | string |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| IsSuccess | boolean |  |
| ErrorMessage | string |  |

Starts a TLS handshake on the link, as a server side of the TLS. The plugin needs to specify the server certificate and its corresponding private key and password. The StartTLSData can contain data that the link has already reported as received but it should be used as part of the TLS handshake. Once the TLS handshake is started by this call, all incoming data is first decrypted before being sent to the OnReceivedData callback, and all outgoing data is queued until the TLS handshake completes, and then sent encrypted over the link. Returns true on success, nil and optional error message on immediate failure.<br/><b>NOTE:</b> The TLS support in the API is currently experimental and shouldn't be considered safe - there's no peer certificate verification and the error reporting is only basic.
