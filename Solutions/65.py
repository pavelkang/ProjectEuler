##pos = 2
##n1 = 3
##n2 = 8
##d1 = 1
##d2 = 3
##while pos<34:
##    factor = pos*2
##    n3 = n1+n2 #11
##    n1 = n2+n3 #19
##    d3 = d1+d2 #4
##    d1 = d2+d3 #7
##    d2 = d1*factor+d3 #
##    n2 = n1*factor+n3
##    n3 = n1+n2
##    pos+=1
##print n1,n2,n3

def calcE(m):
   n, d = m + 1, 1
   for i in xrange(m, 2, -2): n, d, m = n + d + (m - 2) * (d + n + n), d + n + n, m - 2
   return reduce(lambda x, y: int(x) + int(y), str(n * 3 + d * 2))
