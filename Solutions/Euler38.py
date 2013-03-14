l = [1,2,3,4,5,6,7,8,9]
def f(a):
    for item in l:
        if repr(item) not in a: return False
    return True
for i in range(9001,9999):
    a = repr(i)+repr(2*i)
    if f(a): print i,2*i
