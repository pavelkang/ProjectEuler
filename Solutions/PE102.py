# Project Euler 102
# Triangle Containment
data = []
with open("triangles.txt", 'r') as f:
    for line in f.readlines():
        if line.endswith("\n"):
            line = line[:-1]
        data.append(line.split(","))

processed_data = []
for row in data:
    new_row = []
    for number in row:
        new_row.append( eval(number) )
    processed_data.append(new_row)

def cross( v1, v2 ):
    # cross product of two vectors
    return ( v1[1] * v2[0] - v1[0] * v2[1] )

def testLine(line):
    A = ( line[0], line[1] )
    B = ( line[2], line[3] )
    C = ( line[4], line[5] )
    return testTriangle( A, B, C )

def sameSign(a, b,c):
    return (a>0 and b>0 and c>0) or (a<0 and b<0 and c<0)

def testTriangle(A, B, C):
    AO = ( -A[0], -A[1] )
    BO = ( -B[0], -B[1] )
    CO = ( -C[0], -C[1] )
    # test around A
    AB = ( B[0]-A[0], B[1]-A[1] )
    AC = ( C[0]-A[0], C[1]-A[1] )
    # test around B
    BA = ( -AB[0], -AB[1] )
    BC = ( C[0]-B[0], C[1]-B[1] )
    # test around C
    CA = ( -AC[0], -AC[1] )
    CB = ( -BC[0], -BC[1] )
    return (sameSign(cross(AB,AC), cross(AB,AO), cross(AO,AC)) and
            sameSign(cross(BA,BC), cross(BA,BO), cross(BO,BC)) and
            sameSign(cross(CA,CB), cross(CA,CO), cross(CO,CB)))


total = 0
for line in processed_data:
    if testLine(line) == True:
        total += 1
print total
