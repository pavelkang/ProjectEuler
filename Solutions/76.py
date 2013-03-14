import sys
sys.setrecursionlimit(9999999)

def fac(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x*fac(x-1)

def memoize(f):
    def memf(*x):
        if x not in memf.cache:
            memf.cache[x] = f(*x)
        return memf.cache[x]
    memf.cache = {}
    return memf

fac = memoize(fac)

def C(a,b):
    return fac(b)/(fac(a)*fac(b-a))

def floor(x):
    return int(x/2)
    
def g(x,i):
    
        
        


        
