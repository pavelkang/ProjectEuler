# This is module with math helper functions

def gcd(a, b):
    """
    Returns the greatest common denominator.
    """
    a, b= max(a,b), min(a,b)
    if b==0:
        return a
    return gcd(b, a%b)

def isPrime(n):
    """
    Returns True if n is a prime.
    """
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for i in xrange(2, int(n**.5)+1):
            if n % i == 0:
                return False
        return True

def memoize(f):
    """
    Memoization.
    """
    cachedResults = dict()
    def wrapper(*args):
        if args not in cachedResults:
            cachedResults[args] = f(*args)
        return cachedResults[args]
    return wrapper

class priorityQ(object):

    
    def __init__(self, l):
        self.l = l

    def pop(self):
        minIndex = l.index(min(l))
        a = self.l.pop(minIndex)
        return a
    
if __name__ == "__main__":    
    print gcd(120, 50)
    print isPrime(39), isPrime(42), isPrime(13)
