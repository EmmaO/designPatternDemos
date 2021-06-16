'''
The bridge pattern is used to decouple implementations from abstractions.

Kinda.

It's a little hard to understand the use.

Basically, let's say that you have a need for some kind of windowing system.
You want to support macs and windows and linux which means that the windowing system
needs to depend on an abstraction instead of a concrete implementation. But we also
don't have control over any of the concrete implementations - they come from the system.

These implementations are unlikely to conform to any single interface. The names of methods
are likely to vary (draw vs add) and the methods available may be different too 
(drawLine vs drawRect).

The bridge pattern deals with this be definining a series of primitive operations that any viable
window implementation must be able to support. Let's say it's drawLine.

The concrete implementations then must find some way to draw a line. For the first we can invoke
drawLine directly, but for the second we need to create a very thin rectangle.

Either way, by the end of it, we have an abstraction for drawing lines.

Now we make an abstract window class which implements some more full featured operations that can
be made available to concrete window implementations. Here we might define drawRect as a method
that calls drawLine 4 times. We can also expose drawLine directly. We only have access to the 
primitive operations exposed on our previous abstraction.

Finally we'll have concrete window implementations. One for errors might start with a cross in
the corner which we can now draw with a combination of drawRect and drawLine. Another for
alerts might start with an exclamation point.

If we need to add new windows we can do this easily without needing to add additional concrete
implementations for the different window systems.

If we need to support new window systems we can do so by just building out the required primitive
operations.
'''