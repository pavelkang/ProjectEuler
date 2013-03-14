import math
l = []
for a in xrange(2,101):
    for b in xrange(2,101):
        if math.pow(a,b) not in l:
            l.append(math.pow(a,b))
print len(l)
