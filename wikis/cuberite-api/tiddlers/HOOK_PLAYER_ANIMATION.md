This hook is called when the server receives an Animation packet from the client.

For the list of animations that are sent by the client, see the
[Protocol wiki](http://wiki.vg/Protocol#Animation_.28clientbound.29).

## Callback function

The default name for the callback function is OnPlayerAnimation. It has the following signature:

```lua
function MyOnPlayerAnimation(Player, Animation)
```

## Parameters

| Name | Type | Notes |
| --- | --- | --- |
| Player | [cPlayer](#cPlayer) | The player from whom the packet was received |
| Animation | number | The kind of animation |

If the function returns false or no value, the next plugin's callback is called. Afterwards, the
server broadcasts the animation packet to all nearby clients. If the function returns true, no other
callback is called for this event and the packet is not broadcasted.
