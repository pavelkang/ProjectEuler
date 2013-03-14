def f(a,b,n):
    return n**2 + a*n + b

def isPrime(x):
    for i in xrange(2,int(abs(x)**0.5)+1):
        if x%i == 0: return False
    return True

class para(object):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def get(self):
        n = 0
        count = 0
        while isPrime(f(a,b,n)):
            n += 1
            count+= 1
        return count

max = 0
maxa = 0
maxb = 0
for a in range(-1000,0):
    for b in range(1000):
        if para(a,b).get() > max:
            max = para(a,b).get()
            maxa, maxb = a, b
print maxa, maxb
        

