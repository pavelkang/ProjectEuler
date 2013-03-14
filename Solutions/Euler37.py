def f(x):
    l = []
    i = 0
    while x/(10**i)>0:
        l.append(x/(10**i))
        l.append(x%(10**i))
        i += 1
    try: l.pop(l.index(0))
    except: return l
    return l

def memoize(f):
    def memf(*x):
        if x not in memf.cache:
            memf.cache[x] = f(*x)
        return memf.cache[x]
    memf.cache = {}
    return memf

def isPrime(x):
    if x ==1: return False
    if x== 2: return True
    for i in xrange(2,int(x**0.5)+1):
        if x%i == 0: return False
    return True

def isTruPri(x):
    l = f(x)
    for number in l:
        if not isPrime(number): return False
    return True
sume=0
for i in xrange(10,950000):
    if isTruPri(i):
        sume+=i
        print i
print 'sume is', sume        
