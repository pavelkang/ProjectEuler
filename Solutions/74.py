from kmath import *
import itertools

def findRecLen(x):
    d = {x:0}
    for i in itertools.count(1):
        if FacSum(x) not in d:
            d.update({FacSum(x):i})
            x = FacSum(x)
        else:
            return i

count = 342
for i in xrange(867099,1000000):
    if findRecLen(i)==60:
        count += 1
print count
