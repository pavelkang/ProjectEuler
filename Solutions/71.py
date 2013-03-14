from fractions import Fraction
from kmath import *
import math

a = Fraction(3,7)

def find37(n,epsilon):
    m = math.ceil(3.0*n/7)-1
    while not isRP(m,n) :
        if a - Fraction(int(m),int(n)) >= epsilon:
            return -1
        else:
            m -= 1
    return Fraction(int(m),int(n))

epsilon  = 1

for i in xrange(8,1000000):
    if a - find37(i,epsilon)<epsilon:
        epsilon = a- find37(i,epsilon)
        mini = i
print find37(mini,epsilon)
        
