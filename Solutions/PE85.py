# Project Euler 85
def findNumberOfRect(m, n):
    total = 0
    for i in xrange(1,m+1):
        a = m-i+1
        for j in xrange(1,n+1):
            b = n-j+1
            total += a*b
    return total
"""
number = 2000000
min_diff = float("inf")
min_area = 0
for i in xrange(10,100):
    for j in xrange(10,100):
        result = findNumberOfRect(i,j)
        if abs(number-result) < min_diff:
            min_diff = abs(number-result)
            min_area = i*j
print min_area
"""
print findNumberOfRect(1,2000)
