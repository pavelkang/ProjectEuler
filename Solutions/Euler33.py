fractions = []
for a in xrange(2,10):
    for b in xrange(1,a):
        fractions.append([float(b),float(a)])

answer = []
for fraction in fractions:
    for x in xrange(1,10):
        if (fraction[0]*10+x)/(x*10+fraction[1]) == (fraction[0])/(fraction[1]) or (fraction[0]+x*10)/(x+fraction[1]*10) == (fraction[0])/(fraction[1]): 
            answer.append([x,fraction[0],fraction[1]])

print answer
