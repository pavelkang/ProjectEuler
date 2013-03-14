def factor(x):
    factor = []
    for i in xrange(2,int(x**0.5)+1):
        if x%i == 0: factor.append([i,x/i])
    return factor

def test(x):
    l = factor(x)
    standardlist = ['1','2','3','4','5','6','7','8','9']
    for sub in l:
        testlist = []
        for number in repr(x):
            testlist.append(number)
        for element in sub:
            for number in repr(element):
                testlist.append(number)
        if sorted(testlist) == standardlist:
            return True
    return False

answer = 0
for i in xrange(1000,10000):
    if test(i): answer += i

print answer

        
            
    
