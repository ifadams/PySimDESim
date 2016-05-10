# PySimDESim
A simple discrete event simulation framework for teaching and basic modeling. If you're looking for
something more serious (and vastly more developed) there are plenty of great choices out there! For
Python based approaches, SimPY can't be beat http://simpy.readthedocs.io/en/latest/ , and for some *very* heavy weight
(but gigantically powerful) simulation check out ROSS https://github.com/carothersc/ROSS

In SimDESim There are 3 basic elements: the  coordinator, nodes, and actions. The coordinator
(also called the master) maintains the current clock tick, and allows 'out of band' actions to be
applied to nodes. Nodes are elements of the system that maintain state, and can process and generate
actions. Actions are simply messages that nodes can respond to and act on.

The best way to get started is to look at the examples and play around! So far we've included a single
ping-ack communication example. This is a *very* early work, so feel free to report issues or fix bugs
as you find 'em! We'll be slowly adding a few more features and improvements in the future.



