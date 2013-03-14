l = [0,1,2,3,4,5,6,7,8,9]
l1 = []
import string
#D8910 ==> list a
i1 = 1
a = []
while 17*i1 < 1000:
    if 17*i1 < 100:
        a.append('0'+repr(17*i1))
    else:
        if repr(17*i1)[-1] != repr(17*i1)[1] != repr(17*i1)[0]:
            a.append(repr(17*i1))
    i1 +=1

#D567
i2 = 1
b = []
while 7*i2 < 1000:
    if 7*i2 < 100:
        a.append('0'+repr(7*i2))
    else:
        if repr(7*i2)[-1] != repr(7*i2)[1] != repr(7*i2)[0]:
            b.append(repr(7*i2))
    i2 +=1

i3 = 6
c = []
while 2*i3 < 1000:
    if 2*i3 < 100:
        c.append('0'+repr(2*i3))
    else:
        if repr(2*i3)[-1] != repr(2*i3)[1] != repr(2*i3)[0]:
            c.append(repr(2*i3))
    i3 += 1

answer = []
for item1 in a:
    for item2 in b:
        for item3 in c:
            answer.append(item3+item2+item1)

def div(s,divisor):
    if s[0]=='0':
        if eval(s[1:])%divisor ==0: return True
        else: return False
    else:
        if eval(s)%divisor == 0 : return True
        else: return False
print len(answer)
ans = []
for item in answer:
    if div(item[1:4],3) and div(item[2:5],5) and div(item[4:7],11) and div(item[5:8],13):
        ans.append(item)

n = []
for z in ans:
    if string.count(z,'0') <=1 and string.count(z,'1') <=1 and string.count(z,'2') <=1 and string.count(z,'3') <=1 and string.count(z,'4') <=1 and string.count(z,'5') <=1 and string.count(z,'6') <=1 and string.count(z,'7') <=1 and string.count(z,'8') <=1 and string.count(z,'9') <=1:
        n.append(z)
        

print n
    
    
        
    
