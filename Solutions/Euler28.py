import sys
sys.setrecursionlimit(10000)
def p(n):
    if n == 1:
        return 1
    else:
        return p(n-1)+8*n-14

answer = 1
for i in xrange(2,502):
    answer += 4*p(i)+ 6*(2*i-2)

print answer
