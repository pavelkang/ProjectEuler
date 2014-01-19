

def str2int(l):
    L = []
    for element in l:
        L.append(int(element))
    return L

data = []
with open("matrix.txt") as f:
    for line in f.readlines():
        data.append(str2int(line.split(",")))

rows, cols = len(data), len(data[0])

minPath_DIC = {}

for row in xrange(rows):
    minPath_DIC[(row,0)] = data[row][0]

def upOrStay(row, col):
    self = data[row][col]
    stay = self + minPath_DIC[(row,col-1)]
    if row == 0:
        return stay
    else:
        up = minPath_DIC[(row-1,col)] + self        
        return min(stay,up)

def down(row, col):
    self = data[row][col]
    stay = self + minPath_DIC[(row,col-1)]
    if row == rows-1:
        return stay
    else:
        down = minPath_DIC[(row+1,col)] + self        
        return down
"""
for col in xrange(1,cols-1):
    for row in xrange(rows):
        minPath_DIC[(row, col)] = upOrStay(row,col)

for col in xrange(1,cols-1):
    for row in xrange(rows-1,-1,-1):
        result = down(row,col)
        if result < minPath_DIC[(row,col)]:
            minPath_DIC[(row,col)] = result
"""
for col in xrange(1,cols-1):
    for row in xrange(rows):
        minPath_DIC[(row, col)] = upOrStay(row,col)
    for row in xrange(rows-1,-1,-1):
        result = down(row,col)
        if result < minPath_DIC[(row,col)]:
            minPath_DIC[(row,col)] = result    



for row in xrange(rows):
    minPath_DIC[(row,cols-1)] = minPath_DIC[(row,cols-2)] + data[row][cols-1]
            
l = [minPath_DIC[(i,cols-1)] for i in xrange(rows)]            
print min(l)
    















"""
cachedResults = dict()

def memoize(f):
    def wrapper(*args):
        if args not in cachedResults:
            cachedResults[args] = f(*args)
        return cachedResults[args]
    return wrapper

def minPath(row, col):
    self = data[row][col]
    if col == 0:
        return self
    if row == 0:
        down = self+minPath(row+1, col)
        stay = self+minPath(row, col-1)
        return min(down, stay)
    if row = rows-1:
        up = self+minPath(row-1, col)
        stay = self+minPath(row, col-1)
        return min(up, stay)
    if col = cols-1:
        return self+minPath(row, col-1)
    else:
        up = self+minPath(row-1, col)
        down = self+minPath(row+1, col)
        stay = self+minPath(row, col-1)
        return min(up, down, stay)
"""
