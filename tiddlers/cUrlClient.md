Implements high-level asynchronous access to URLs, such as downloading webpages over HTTP(S).

Note that unlike other languages' URL access libraries, this class implements asynchronous requests.
This means that the functions only start a request and return immediately. The request is then
fulfilled in the background, while the server continues to run. The response is delivered back to the
plugin using callbacks. This allows the plugin to start requests and not block the server until the
response is received.

The functions that make network requests are all static and have a dual interface. Either you can use
a single callback function, which gets called once the entire response is received or an error is
encountered. Or you can use a table of callback functions, each function being called whenever the
specific event happens during the request and response lifetime. See the Simple Callback and Callback
Table chapters later on this page for details and examples.

All the request function also support optional parameters for further customization of the request -
the Headers parameter specifies additional HTTP headers that are to be sent (as a dictionary-table of
key -> value), the RequestBody parameter specifying the optional body of the request (used mainly for
POST and PUT requests), and an Options parameter specifying additional options specific to the protocol
used.

## Functions

### Overload 1: **Static** Delete(URL, Callbacks, [Headers], [RequestBody], [Options])

| Name | Type | Notes |
| --- | --- | --- |
| URL | string |  |
| Callbacks | table |  |
| Headers (optional) | table |  |
| RequestBody (optional) | string |  |
| Options (optional) | table |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| IsSuccess | boolean |  |
| ErrorMessagge | string |  |

Starts a HTTP DELETE request. Alias for Request("DELETE", ...). Returns true on succes, false and error message on immediate failure (unparsable URL etc.).

### Overload 2: **Static** Delete(URL, Callbacks)

| Name | Type | Notes |
| --- | --- | --- |
| URL | string |  |
| Callbacks | function |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| IsSuccess | boolean |  |
| ErrorMessagge | string |  |

Starts a HTTP DELETE request. Alias for Request("DELETE", ...). Returns true on succes, false and error message on immediate failure (unparsable URL etc.).

### Overload 1: **Static** Get(URL, Callbacks, [Headers], [RequestBody], [Options])

| Name | Type | Notes |
| --- | --- | --- |
| URL | string |  |
| Callbacks | table |  |
| Headers (optional) | table |  |
| RequestBody (optional) | string |  |
| Options (optional) | table |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| IsSuccess | boolean |  |
| ErrMsg | string |  |

Starts a HTTP GET request. Alias for Request("GET", ...). Returns true on succes, false and error message on immediate failure (unparsable URL etc.).

### Overload 2: **Static** Get(URL, Callbacks)

| Name | Type | Notes |
| --- | --- | --- |
| URL | string |  |
| Callbacks | function |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| IsSuccess | boolean |  |
| ErrMsg | string |  |

Starts a HTTP GET request. Alias for Request("GET", ...). Returns true on succes, false and error message on immediate failure (unparsable URL etc.).

### Overload 1: **Static** Post(URL, Callbacks, [Headers], [RequestBody], [Options])

| Name | Type | Notes |
| --- | --- | --- |
| URL | string |  |
| Callbacks | table |  |
| Headers (optional) | table |  |
| RequestBody (optional) | string |  |
| Options (optional) | table |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| IsSuccess | boolean |  |
| ErrMsg | string |  |

Starts a HTTP POST request. Alias for Request("POST", ...). Returns true on succes, false and error message on immediate failure (unparsable URL etc.).

### Overload 2: **Static** Post(URL, Callbacks)

| Name | Type | Notes |
| --- | --- | --- |
| URL | string |  |
| Callbacks | function |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| IsSuccess | boolean |  |
| ErrMsg | string |  |

Starts a HTTP POST request. Alias for Request("POST", ...). Returns true on succes, false and error message on immediate failure (unparsable URL etc.).

### Overload 1: **Static** Put(URL, Callbacks, [Headers], [RequestBody], [Options])

| Name | Type | Notes |
| --- | --- | --- |
| URL | string |  |
| Callbacks | table |  |
| Headers (optional) | table |  |
| RequestBody (optional) | string |  |
| Options (optional) | table |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| IsSuccess | boolean |  |
| ErrMsg | string |  |

Starts a HTTP PUT request. Alias for Request("PUT", ...). Returns true on succes, false and error message on immediate failure (unparsable URL etc.).

### Overload 2: **Static** Put(URL, Callbacks)

| Name | Type | Notes |
| --- | --- | --- |
| URL | string |  |
| Callbacks | function |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| IsSuccess | boolean |  |
| ErrMsg | string |  |

Starts a HTTP PUT request. Alias for Request("PUT", ...). Returns true on succes, false and error message on immediate failure (unparsable URL etc.).

### **Static** Request(Method, URL, Callbacks, [Headers], [RequestBody], [Options])

| Name | Type | Notes |
| --- | --- | --- |
| Method | string |  |
| URL | string |  |
| Callbacks | table |  |
| Headers (optional) | table |  |
| RequestBody (optional) | string |  |
| Options (optional) | table |  |

**Returns:**

| Name | Type | Notes |
| --- | --- | --- |
| IsSuccess | boolean |  |
| ErrMsg | string |  |

Starts a request with the specified Method. Returns true on succes, false and error message on immediate failure (unparsable URL etc.).

## Additional Info

### Simple Callback

When you don't need fine control for receiving the requests and are interested only in the result,
you can use the simple callback approach. Pass a single function as the Callback parameter, the
function will get called when the response is fully processed, either with the body of the response,
or with an error message:

```
cUrlClient:Get(url,
	function (a_Body, a_Data)
		if (a_Body) then
			-- Response received correctly, a_Body contains the entire response body,
			-- a_Data is a dictionary-table of the response's HTTP headers
		else
			-- There was an error, a_Data is the error message string
		end
	end
)
```

### Callback Table

To provide complete control over the request and response handling, Cuberite allows plugins to pass
a table of callbacks as the Callback parameter. Then the respective functions are called for their
respective events during the lifetime of the request and response. This way it is possible to
process huge downloads that wouldn't fit into memory otherwise, or display detailed progress.
Each callback function receives a "self" as its first parameter, this allows the functions to
access the Callback table and any of its other members, allowing the use of Lua object idiom for
the table. See [this forum post](https://forum.cuberite.org/thread-2062.html) for an
example.

The following callback functions are used by Cuberite. Any callback that is not assigned is
silently ignored. The table may also contain other functions and other values, those are silently
ignored.

| Callback | Params | Notes |
| --- | --- | --- |
| OnConnected | self, {{cTCPLink}}, RemoteIP, RemotePort | Called when the connection to the remote host is established. *Note that current implementation doesn't provide the {{cTCPLink}} parameter and passes nil instead.* |
| OnCertificateReceived | self | Called for HTTPS URLs when the server's certificate is received. If the callback returns anything else than true, the connection is aborted. *Note that the current implementation doesn't provide the certificate because there is no representation for the cert in Lua.* |
| OnTlsHandshakeCompleted | self | Called for HTTPS URLs when the TLS is established on the connection. |
| OnRequestSent | self | Called after the entire request is sent to the server. |
| OnStatusLine | self, HttpVersion, StatusCode, Rest | The initial line of the response has been parsed. HttpVersion is typically "HTTP/1.1", StatusCode is the numerical HTTP status code reported by the server (200 being OK), Rest is the rest of the line, usually a short message in case of an error. |
| OnHeader | self, Name, Value | A new HTTP response header line has been received. |
| OnHeadersFinished | self, AllHeaders | All HTTP response headers have been parsed. AllHeaders is a dictionary-table containing all the headers received. |
| OnBodyData | self, Data | A piece of the response body has been received. This callback is called repeatedly until the entire body is reported through its Data parameter. |
| OnBodyFinished | self | The entire response body has been reported by OnBodyData(), the response has finished. |
| OnError | self, ErrorMsg | Called whenever an error is detected. After this call, no other callback will get called. |
| OnRedirecting | self, NewUrl | Called if the server returned a valid redirection HTTP status code and a Location header, and redirection is allowed by the Options. |

The following example is adapted from the Debuggers plugin's "download" command, it downloads the
contents of an URL into a file.

```
function HandleConsoleDownload(a_Split)  -- Console command handler
	-- Read the params from the command:
	local url = a_Split[2]
	local fnam = a_Split[3]
	if (not(url) or not(fnam)) then
		return true, "Missing parameters. Usage: download  "
	end

	-- Define the cUrlClient callbacks
	local callbacks =
	{
		OnStatusLine = function (self, a_HttpVersion, a_Status, a_Rest)
			-- Only open the output file if the server reports a success:
			if (a_Status ~= 200) then
				LOG("Cannot download " .. url .. ", HTTP error code " .. a_Status)
				return
			end
			local f, err = io.open(fnam, "wb")
			if not(f) then
				LOG("Cannot download " .. url .. ", error opening the file " .. fnam .. ": " .. (err or ""))
				return
			end
			self.m_File = f
		end,

		OnBodyData = function (self, a_Data)
			-- If the file has been opened, write the data:
			if (self.m_File) then
				self.m_File:write(a_Data)
			end
		end,

		OnBodyFinished = function (self)
			-- If the file has been opened, close it and report success
			if (self.m_File) then
				self.m_File:close()
				LOG("File " .. fnam .. " has been downloaded.")
			end
		end,
	}

	-- Start the URL download:
	local isSuccess, msg = cUrlClient:Get(url, callbacks)
	if not(isSuccess) then
		LOG("Cannot start an URL download: " .. (msg or ""))
		return true
	end
	return true
end
```

### Options

The requests support the following options, specified in the optional Options table parameter:

| Option name | Description |
| --- | --- |
| MaxRedirects | Maximum number of HTTP redirects that the cUrlClient will follow. If the server still reports a redirect after reaching this many redirects, the cUrlClient reports an error. May be specified as either a number or a string parsable into a number. Default: 30. |
| OwnCert | The client certificate to use, if requested by the server. A string containing a PEM- or DER-encoded cert is expected. |
| OwnPrivKey | The private key appropriate for OwnCert. A string containing a PEM- or DER-encoded private key is expected. |
| OwnPrivKeyPassword | The password for OwnPrivKey. If not present or empty, no password is assumed. |
| TrustedRootCAs | The certificates of the Root CAs that are to be trusted, encoded in PEM format. Multiple certificates can be used by concatenating the certificates, separating them by newlines. If this option is not present or empty, the request will NOT check the server's certificate, which is UNSAFE! |

Redirection:

* If a redirect is received, and redirection is allowed by MaxRedirects, the redirection is
  reported via OnRedirecting() callback and the request is restarted at the redirect URL, without
  reporting any of the redirect's headers nor body.
* If a redirect is received and redirection is not allowed (maximum redirection attempts have
  been reached), the OnRedirecting() callback is called with the redirect URL and then the request
  terminates with an OnError() callback, without reporting the redirect's headers nor body.
