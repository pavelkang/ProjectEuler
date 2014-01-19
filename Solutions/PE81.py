from kmath import *

def str2int(l):
    L = []
    for element in l:
        L.append(int(element))
    return L


data = []

with open("matrix.txt") as f:
    for line in f.readlines():
        data.append(str2int(line.split(",")))


cachedResults = dict()
def memoize(f):
    """
    Memoization.
    """

    def wrapper(*args):
        if args not in cachedResults:
            cachedResults[args] = f(*args)
        return cachedResults[args]
    return wrapper


def minPathSum(row, col):
    if row == 0 and col == 0:
        return 131
    if row == 0:
        result = 0
        for COL in xrange(0, col+1):
            result += data[0][COL]
        return result
    if col == 0:
        result = 0
        for ROW in xrange(0, row+1):
            result += data[ROW][0]
        return result
    return min( minPathSum(row-1, col), minPathSum(row, col-1) ) + data[row][col]

minPathSum = memoize(minPathSum)

print minPathSum(79, 79)    
