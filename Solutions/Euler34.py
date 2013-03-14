import sys
sys.setrecursionlimit(10000000)

def fac(x):
    if x==0: return 1
    return fac(x-1)*x

facList = []
for i in xrange(0,10):
    facList.append(fac(i))

def test(x):
    sumOfFac = 0
    for number in repr(x):
        sumOfFac += facList[int(number)]
    if sumOfFac == x: return True
    else: return False

for x in xrange(100,1000000):
    if test(x): print x


