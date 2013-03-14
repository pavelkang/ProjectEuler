import sys
sys.setrecursionlimit(999999)

open('triangle.txt')
l = []
for line in file('triangle.txt','r'):
    l.append(map(int,line.strip('\n').split()))

def find(j,i):
    if j == 0 and i == 0:
        return l[0][0]
    elif i == 0 and j != 0:
        return find(j-1,i)+l[j][i]
    elif i == len(l[j])-1 and j!=0:
        return find(j-1,i-1)+l[j][i]
    else:
        return max(find(j-1,i-1),find(j-1,i))+l[j][i]
    
def memoize(f):
    def memf(*x):
        if x not in memf.cache:
            memf.cache[x] = f(*x)
        return memf.cache[x]
    memf.cache = {}
    return memf
find = memoize(find)
ma = 0
for i in xrange(0,100):
    if find(99,i)>ma:
        ma = find(99,i)
print ma

count = 0
for j in xrange(0,100):
