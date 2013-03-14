l=[]
for x in xrange(1,1000):
    for y in xrange(1,int((1000**2-x**2)**0.5)+1):
        if round((x**2+y**2)**0.5) == (x**2+y**2)**0.5:
            l.append([x,y,(x**2+y**2)**0.5])

def f(x):
    s = 0
    for i in x:
        s += i
    return s

d={}
for item in l:
    if f(item) > 1000: l.pop(l.index(item))
    else:
        if d.has_key(f(item)):
            d[f(item)]+=1
        else:
            d[f(item)]=1

maxe = 0
for i in d:
    if d[i]>maxe:
        maxe=d[i]
        big = repr(i)
print maxe,big
