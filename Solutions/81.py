import sys
sys.setrecursionlimit(999999)
matrix = open('matrix.txt')
l = []
for line in matrix:
    l.append(line.strip('\n').split(','))

def mini(i,j):
    if i==0 and j == 0 :
        return int(l[0][0])
    if i!=0 and j == 0 :
        return int(l[i][0]) + mini(i-1,0)
    if i==0 and j != 0 :
        return int(l[0][j])+ mini(0,j-1)
    if i!=0 and j!= 0 :
        return int(l[i][j]) + min(int(mini(i-1,j)),int(mini(i,j-1)))

def memoize(f):
    def memf(*x):
        if x not in memf.cache:
            memf.cache[x] = f(*x)
        return memf.cache[x]
    memf.cache = {}
    return memf

mini=memoize(mini)
print mini(79,79)
    
