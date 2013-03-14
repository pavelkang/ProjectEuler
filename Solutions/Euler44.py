PenList = []
for n in xrange(1,2000):
    PenList.append(n*(3*n-1)/2)

ans = []
mini = 99999999999
a = 0
while a<len(PenList):
    itemA = PenList[a]
    for itemB in PenList[a:]:
        if ((itemA + itemB) in PenList) and (abs(itemA-itemB) in PenList):
            if abs(itemA-itemB) < mini:
                mini = abs(itemA - itemB)
                ans = [itemA,itemB]
    a+=1
print ans, mini
                
