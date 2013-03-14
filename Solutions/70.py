from kmath import *
import time

minv=11
i = 87109
a = time.clock()
for i in xrange(8319823,10**7):
    if len(repr(i)) == len(repr(int(EulerPhi(i)))):
    ##    if isPermutation(repr(i),repr(int(EulerPhi(i)))):
        if isPer(repr(i),repr(int(EulerPhi(i)))):
            if float(i)/float(EulerPhi(i))<minv:
                minv = float(i)/float(EulerPhi(i))
                mini = i
b = time.clock()
print 'mini is {0},rakes {1}'.format(mini,b-a)



