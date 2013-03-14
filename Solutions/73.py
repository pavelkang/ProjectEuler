import math
from kmath import *
def f(x):
    lowerBound = int(math.floor(x/3.0)+1)                     
    upperBound = int(math.floor(x/2.0+0.5))
    count = 0 
    for i in xrange(lowerBound,upperBound):
        if isRP(i,x):
            count+=1
    return count

count = 0
for i in xrange(2,12001):
    count += f(i)
print count
