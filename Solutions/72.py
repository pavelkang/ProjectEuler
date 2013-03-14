from kmath import *
count = 0
for i in xrange(2,1000001):
    count += EulerPhi(i)
print count
