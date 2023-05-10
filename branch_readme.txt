we've got a first implementation of some x cards - whirlwind and skewer
* part of how they function is by setting energy to 0 after play, this _should_ work but theoretically could have a weird consequence or two, though I've added a test for the case I know of
* the actual problem: we don't actually play skewer ingame (didn't test whirlwind).
* I think this is because X-cost cards are reported as having a cost of -1 by comm mod, which is how we treat unplayable cards, which could make us think it's unplayable

I think we'll need to implement x cards properly, but that's not something I'm gonna do now, so putting what I've got so far onto a branch