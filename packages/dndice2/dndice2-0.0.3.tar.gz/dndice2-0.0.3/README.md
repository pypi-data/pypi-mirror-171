Small DnD dice package

from dndice2.dice import *

or

from dndice2.dice import d4, d6, d8, d10, 12, d20, d100, d, maker

has maker function that let's you make new dice:

example:

d50 = maker(50)

d50() "returns 1 - 50"
