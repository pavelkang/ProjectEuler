from kmath import *
import sys
def getPrimeWays(n, m):
    """
    Returns how many ways to write n as a sum of PRIME numbers whose values are at least m
    """
    if isPrime(m) == False:
        return 0
    if m > n/2.0:
        return 0
    else:
        result = 1 if isPrime(n-m) else 0
        for i in xrange(m, n-m+1):
            result += getPrimeWays(n-m, i)
        return result

getPrimeWays = memoize(getPrimeWays)        
        
def count(n):
    """
    Count the number of ways a number can be written as the sum of at least two positives.
    """
    result = 0
    for i in xrange(1, n/2+1):
        result += getPrimeWays(n, i)
    return result

n = 10
ways = count(n)
while ways <= 5000:
    n += 1
    ways = count(n)
print n
