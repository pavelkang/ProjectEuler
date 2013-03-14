import sys
sys.setrecursionlimit(999999)
matrix = open('matrix2.txt')
l = []
for line in matrix:
    l.append(line.strip('\n').split(','))

def mini(i,j):
    if j==0:
        return int(l[i][j])
    if i==79:
        return l[i][j] + min(int(mini(i,j-1)),int(mini(i-1,j)))    
    if j!=0 and i==0:
        return int(l[i][j]) + min(int(mini(i,j-1)),int(mini(i+1,j)))
    
    if j!=0 and i!=0:
        return int(l[i][j]) + min(int(mini(i,j-1)),int(mini(i+1,j)),int(mini(i-1,j)))

def memoize(f):
    def memf(*x):
        if x not in memf.cache:
            memf.cache[x] = f(*x)
        return memf.cache[x]
    memf.cache = {}
    return memf

mini=memoize(mini)

minValue = 99999999
for i in xrange(0,79):
    if mini(i,79) < minValue:
        minValue = mini(i,79)
print minValue


