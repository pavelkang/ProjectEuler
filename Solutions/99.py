import math
exp = open('exp.txt','r')
l = []
for line in exp:
    l.append(line.strip('\n').split(','))

def f(x):
    return int(x[1])*math.log(int(x[0]))

maxValue = 0
for number in xrange(0,len(l)):
    if f(l[number]) > maxValue:
        maxValue = f(l[number])
        maxLine = number

    
