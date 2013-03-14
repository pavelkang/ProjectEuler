l = [1,2,3,4,5,6,7]
def f(x):
    for item in l:
        if repr(item) not in repr(x): return False
    return True

def isPrime(x):
    if x ==1: return False
    if x== 2: return True
    for i in xrange(2,int(x**0.5)+1):
        if x%i == 0: return False
    return True

l2=[]
for i in xrange(1234567,7654321):
    if f(i) and isPrime(i): print i

