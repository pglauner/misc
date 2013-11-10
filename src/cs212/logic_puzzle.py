'''
Created on Nov 10, 2013

@author: pglauner
'''
import itertools


def answer(**names):
    return sorted(names, key=lambda name: names[name])


def day_after(after, before):
    return after is before + 1


def match(a1, a2, b1, b2):
    return (a1 is b1 and a2 is b2) or (a1 is b2 and a2 is b1)


def logic_puzzle():
    days = [monday, tuesday, wednesday, thursday, friday] = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(days))
    return next(answer(Wilkes=WILKES, Hamming=HAMMING, Minsky=MINSKY, Knuth=KNUTH, Simon=SIMON)
                for (laptop, droid, tablet, iphone, _) in orderings
                if wednesday is laptop#1
                if friday is not tablet#8
                if (iphone == tuesday) ^ (tablet == tuesday)#12
                for (programmer, writer, manager, designer, _) in orderings
                if designer is not droid#9
                if thursday is not designer#7
                for (HAMMING, KNUTH, MINSKY, SIMON, WILKES) in orderings
                if programmer is not WILKES#2
                if match(programmer, droid, WILKES, HAMMING)#3
                if writer is not MINSKY#4
                if KNUTH is not manager and tablet is not manager#5
                if day_after(KNUTH, SIMON)#6
                if day_after(KNUTH, manager)#10
                if match(laptop, WILKES, monday, writer)#11
                )


if __name__ == '__main__':
    print logic_puzzle()
