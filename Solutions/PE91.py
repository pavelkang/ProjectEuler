class unorderedTuple(object):
    
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def __eq__(self, other):
        return ((self.a==other.a and self.b==other.b) or
                (self.a==other.b and self.b==other.a))

    def hypoSqr(self):
        return self.a**2 + self.b**2

    def __sub__(self, other):
        return unorderedTuple( abs(self.a-other.a), abs(self.b-other.b) )

    def __str__(self):
        return "(%d, %d)" %(self.a, self.b)

    def __repr__(self):
        return "(%d, %d)" %(self.a, self.b)        

    def __hash__(self):
        small, big = min(self.a, self.b), max(self.a, self.b)
        return 10*small + big
        
def makeDic():
    d = dict()
    for i in xrange(0,51):
        for j in xrange(0,51):
            t = unorderedTuple(i,j)
            d[t] = t.hypoSqr()
    return d

def isRecTri(a,b,c):
    """ a, b, c is the square of three sides. """
    if a==0 or b==0 or c==0:
        return False
    return ( a+b==c or a+c==b or b+c==a)

def tuple2Unorder(t):
    return unorderedTuple(t[0],t[1])
    
def findTris():
    M = 2
    v1 = set()
    D = makeDic()
    count = 0
    for x in xrange(0,M+1):
        for y in xrange(0,M+1):
            if x == 0 and y == 0:
                pass
            else:
                v1.add((x,y))
    for v in v1:
        for k in v1:
            l0 = tuple2Unorder(v)
            l1 = tuple2Unorder(k)
            a = D[l0]
            b = D[l1]
            c = D[l0-l1]
            if isRecTri(a,b,c):
                count += 1
    return count/2
print findTris()    
