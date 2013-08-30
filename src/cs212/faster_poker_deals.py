import itertools
import random
import timeit

mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC']

def deal1(numhands, n=5, deck=mydeck):
    cards = random.sample(deck, numhands * n)
    return zip(*[iter(cards)]*n)

def deal_sample(numhands, n=5, deck=mydeck):
    random.shuffle(deck)
    return [deck[n*i:n*(i+1)] for i in range(numhands)]

products = ((p1, p2) for p1, p2 in itertools.product(xrange(1,len(mydeck)+1), repeat=2) if p1*p2 <= 52)

funcs = ('deal1', 'deal_sample')
times = [[] for f in funcs]
idxs = xrange(len(funcs))
for p1, p2 in products:
    local_times = [timeit.repeat('%s(%s, %s)' % (f, p1, p2), 'from __main__ import %s' % f, number=1, repeat=100) for f in funcs]
    map(lambda i: times[i].extend(*[local_times[i]]), idxs)
   
for t in times:
    print 'min=%s    max=%s    avg=%s' % (min(t), max(t), sum(t)/len(t))

# Optional numpy part to visualize distribution
import matplotlib.pyplot as plt
map(lambda i: plt.hist(times[i], bins=20, alpha=0.5, label=funcs[i]), idxs)
plt.xlabel("Time")
plt.ylabel("Frequency")
plt.legend()
plt.show()