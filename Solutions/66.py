import itertools, math
def isS(x):
    if int(x**0.5)==x**0.5:
        return True
    else:
        return False

def f(D):
    for i in itertools.count(1):
        if isS(D*(i**2)+1):
            return math.pow(D*(i**2)+1,0.5)

maxx = 0
maxD = 0
i = 0
ii = 0
for D in xrange(62,1001):
    if i == 10:
        i = 0
        print ii
        ii +=1
    if not isS(D):
        if f(D)>maxx:
            maxx = f(D)
            maxD = D
    i+=1

