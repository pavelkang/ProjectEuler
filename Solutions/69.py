from kmath import isRP,isPrime
import time
def PrimeFactor(x):
    factors = []
    if x%2 == 0 :
        factors.append(2)
        while x%2 == 0:
            x = x/2
    for i in xrange(1,int(x**0.5)+1):
        if x%i==0:
            if isPrime(i):factors.append(i)
            if isPrime(x/i):factors.append(x/i)    
    return list(set(factors))
def EulerPhi(x):
    l = PrimeFactor(x)
    ans = x
    for item in l:
        ans *= float(1-1.0/float(item))
    return ans

maxNOverPhi = 0
maxi = 0
start = time.clock()
for i in xrange(10,100,2):
    if float(i)/float(EulerPhi(i))>maxNOverPhi:
        maxNOverPhi = float(i)/float(EulerPhi(i))
        maxi = i
end = time.clock()
print 'max ratio is {0}, and max n is {1}'.format(maxNOverPhi,maxi)
print 'runs {0}'.format(end-start)
