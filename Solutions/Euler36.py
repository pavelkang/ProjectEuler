def reverse(s):
    l = []
    for number in s:
        l = [number] + l
    return ''.join(l)
        
def isPalin(x):
    if repr(x).startswith('0'): return False
    if reverse(repr(x)) == repr(x): return True
    else: return False

#answer = 0
#for i in xrange(1,1000000):
 #   if isPalin(i) and isPalin(int(bin(i)[2:])):
  #      print i

   #     answer += i

#print answer
