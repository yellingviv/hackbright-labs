Ubermelon is harvesting!

This lab is focused on working with and familiarizing ourselves with classes. We are creating classes of different melons carried by Ubermelon, and then also a class of Melons for the harvest that is happening. We are analyzing the melons for sellability and reporting back.

I struggled with creating the second class, Melon, and how it relates to the original class, MelonType (particularly since Melon was not a _child_ class of MelonType). Getting used to the ways in which we were passing objects that would print some unusual content to the console when it doing the right thing was also a struggle (e.g. with the `make_melons(make_melon_types())` output, we received `[<__main__.Melon object at 0x10e68ff10>, <__main__.Melon object at 0x10e68ff50>, <__main__.Melon object at 0x10e68ff90>, <__main__.Melon object at 0x10e68ffd0>, <__main__.Melon object at 0x10e5e8050>, <__main__.Melon object at 0x10e5e80d0>, <__main__.Melon object at 0x10e5e8110>, <__main__.Melon object at 0x10e5e8150>, <__main__.Melon object at 0x10e5e8190>]` which threw me off and resulted in me trying to troubleshoot until I realized it was actually what I wanted and I could then work with those objects).

Calling the method is_sellable on the Melon class was also confusing at first, as I was making a lot of mistakes with passing correctly or incorrectly, forgetting parentheses, etc.

This was one of our harder labs so far and I'm looking forward to doing a lot more practice with classes to get better at them.
