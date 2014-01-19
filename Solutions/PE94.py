# Project Euler 94
# Almost Equilateral Triangles
# Kai Kang
from kmath import gcd
hypos = dict()

mlimit = 12910
for m in xrange(2, mlimit):
    for n in xrange(1, m):
        if (n+m)%2 == 1 and gcd(n, m) == 1:
            a = m**2 - n**2
            b = 2*m*n
            c = m**2 + n**2
            hypos[c] = (a,b)

total = 0
for a in xrange(3,333333334,2):
    b = a - 1
    c = a + 1
    # triangle (a, a, b) or (a, a, c)
    try:
        A = hypos[a]
        if b in A:
            total += 1
        if c in A:
            total += 1
    except:
        pass
print total
