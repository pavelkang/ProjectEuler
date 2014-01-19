# Project Euler 86

M = 100
perfect_squares = set()
for a in xrange(1,int(2.24*M)):
    perfect_squares.add(a**2)

def f(M):
    number = 0
    for a in xrange(1,M+1):
        for b in xrange(1,a+1):
            for c in xrange(1,b+1):
                result = (b+c)**2+a**2
                if result in perfect_squares:
                    number += 1
    return number


