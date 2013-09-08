'''
Created on Sep 8, 2013

@author: pglauner
'''

def slow_inverse(f, delta=1/128.):
    """Given a function y = f(x) that is a monotonically increasing function on
    non-negative numbers, return the function x = f_1(y) that is an approximate
    inverse, picking the closest value to the inverse, within delta."""
    def f_1(y):
        x = 0
        while f(x) < y:
            x += delta
        # Now x is too big, x-delta is too small; pick the closest to y
        return x if (f(x)-y < y-f(x-delta)) else x-delta
    return f_1 


def inverse(f, delta = 1/128.):
    """Given a function y = f(x) that is a monotonically increasing function on
    non-negative numbers, return the function x = f_1(y) that is an approximate
    inverse, picking the closest value to the inverse, within delta."""
    def f_1(y):
        low, high = 0, float(y)
        last, mid = 0, (low + (high - low) / 2.)
        while abs(last - mid) > delta:
            if f(mid) < y:
                low = mid + delta
            elif f(mid) > y:
                high = mid - delta
            else:
                return mid
            last, mid = mid, (low + (high - low) / 2)
        return mid if (f(mid)-y < y-f(mid-delta)) else mid-delta
    return f_1


def inverse_newton(f, delta = 1/128.):
    """Given a function y = f(x) that is a monotonically increasing function on
    non-negative numbers, return the function x = f_1(y) that is an approximate
    inverse, picking the closest value to the inverse, within delta."""
    def _derivative(func): return lambda x: (func(x + delta) - func(x)) / delta
    def _diff(y): return lambda x: f(x) - y
    def newton(y, n=50):
        x = float(y) / 2
        diff_func = _diff(y)
        deri_func = _derivative(diff_func)
        for _ in xrange(n):
            x = x - diff_func(x) / deri_func(x)
        return x
    return newton


if __name__ == '__main__':
    def square(x): return x*x
    sqrt, sqrt1, sqrt2 = slow_inverse(square), inverse(square), inverse_newton(square)
    def special(x): return x - 2*x + 0.012345*x*x*x
    s, s1, s2 = slow_inverse(special), inverse(special), inverse_newton(special)
    N = 1000000000

    print sqrt(N)
    print sqrt1(N)
    print sqrt2(N)

    print s(N)
    print s1(N)
    print s2(N)
