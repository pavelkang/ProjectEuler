from decimal import *

getcontext().prec = 100

def findHundredDecSum(n):
    n = Decimal(n)
    s = str(n**Decimal(.5))
    result = 0
    for element in s:
        if element == ".":
            continue
        result += int(element)
    return result
print findHundredDecSum(2)
    
total = 0    
for i in xrange(1, 101):
    total += findHundredDecSum(i)
print total

