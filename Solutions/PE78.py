from kmath import *
import sys

def getWays(n, m):
    """
    Returns how many ways to write n as a sum of numbers whose values are at least m
    """
    if m > n/2.0:
        return 0
    else:
        result = 1
        for i in xrange(m, n-m+1):
            result += getWays(n-m, i)
        return result

getWays = memoize(getWays)

def count(n):
    """
    Count the number of ways a number can be written as the sum of at least two positives.
    """
    result = 1
    for i in xrange(1, n/2+1):
        result += getWays(n, i)
    return result

"""
while count(n) % 1000000 != 0:
    n+= 1
print n    
"""
