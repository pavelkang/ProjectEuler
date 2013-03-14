import math

def test(x):
    a = str(x)
    sum = 0
    for digit in a:
        sum += math.pow(float(digit),5)
    return sum== x
        
i = 10
s = 0
while i < 1000000:
    if test(i): s += i
    i += 1
print s
