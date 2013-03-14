triL = []
penL = []
hexL = []
for n in xrange(1,99999):
    triL.append(0.5*n*(n+1))
    penL.append(0.5*n*(3*n-1))
    hexL.append(n*(2*n-1))
i = 286
while not ((triL[i] in penL) and (triL[i] in hexL)):
    i += 1
print triL[i]
