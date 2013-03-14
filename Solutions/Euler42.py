import string

triL = []
for i in xrange(99999):
    triL.append(0.5*i*(i+1))

def ind(x):
    return x.index('"')
f = open('words.txt')
lw=[]
text = f.readline()
i = 0
while i < len(text):
    if text[i] == '"':
        p = text[(i+1):].index('"') + i
        lw.append(text[i+1:p+1])
        i = p+2
    else:
        i+=1
        
f.close()

def wTOn(x):
    n = 0
    for char in x: 
        if char in string.ascii_uppercase:
            n += string.ascii_uppercase.index(char)+1
        
    return n

number=0
for item in lw[0:-1]:
    if wTOn(item) in triL: number +=1
print number
