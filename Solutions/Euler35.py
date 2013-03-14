

def isPrime(x):
    if x ==1: return False
    if x== 2: return True
    for i in xrange(2,int(x**0.5)+1):
        if x%i == 0: return False
    return True

