# Project Euler 75
"""
from Vector import *
from Matrix import *

U1 = Matrix([ [ 1,  2,  2],
              [-2, -1, -2],
              [ 2,  2,  3] ])
U2 = Matrix([ [ 1, 2, 2],
              [ 2, 1, 2],
              [ 2, 2, 3] ])
U3 = Matrix([ [-1, -2, -2],
              [2, 1, 2],
              [2, 2, 3] ])
base = Vector([3, 4, 5])
"""
from kmath import gcd

limit = 1500000
triangles = [0]*(limit+1)

mlimit = int((limit/2)**.5)

for m in xrange(2, mlimit):
    for n in xrange(1, m):
        if (n+m)%2 == 1 and gcd(n, m) == 1:
            a = m**2 - n**2
            b = 2*m*n
            c = m**2 + n**2
            p = a+b+c
            while p <= limit:
                if triangles[p] == 0:
                    triangles[p] += 1
                elif triangles[p] == 1:
                    triangles[p] = -1
                elif triangles[p] == -1:
                    pass
                p += a+b+c

print triangles.count(1)
