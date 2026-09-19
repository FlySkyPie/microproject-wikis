This hook is called when the current weather has expired and a new weather is selected. Plugins may
override the new weather being set.

The new weather setting is sent to the clients only after this hook has been processed.

See also the {{OnWeatherChanged|HOOK_WEATHER_CHANGED}} hook for a similar hook called after the
change.

## Callback function

The default name for the callback function is OnWeatherChanging. It has the following signature:

```lua
function MyOnWeatherChanging(World, Weather)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| World | [cWorld](#cWorld) | World for which the weather is changing |
| Weather | number | The newly selected weather. One of wSunny, wRain, wStorm |

The hook handler can return up to two values. If the first value is false or not present, the server
calls other plugins' callbacks and finally sets the weather. If it is true, the server doesn't call any
more callbacks for this hook. The second value returned is used as the new weather. If no value is
given, the weather from the parameters is used as the weather. Returning false as the first value and a
specific weather constant as the second value makes the server call the rest of the hook handlers with
the new weather value.
