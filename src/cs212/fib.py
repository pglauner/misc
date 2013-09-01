'''
Created on Sep 1, 2013

@author: pglauner
'''

from my_decorators import countcalls, memo, callcounts


@countcalls
def fib(n):
    return 1 if n <= 1 else fib(n-1) + fib(n-2)


@countcalls
@memo
def fib_memo(n):
    return 1 if n <= 1 else fib_memo(n-1) + fib_memo(n-2)


def test_fib(n_max=30):
    calls_previous = 1
    for n in range(n_max+1):
        res = fib(n)
        calls = callcounts[fib]
        print n, res, calls, float(calls) / calls_previous
        calls_previous = calls
        callcounts[fib] = 0


def test_fib_memo(n_max=30):
    calls_previous = 1
    for n in range(n_max+1):
        res = fib_memo(n)
        calls = callcounts[fib_memo]
        print n, res, calls, float(calls) / calls_previous
        calls_previous = calls


if __name__ == '__main__':
    test_fib(30)
    print
    test_fib_memo(30)
