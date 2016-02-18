import sys, os

# line equation between two points
def lequ(p1,p2):
    if p2[0]!=p1[0]:
        tan = float(p2[1]-p1[1])/float(p2[0]-p1[0])
        y = float(p2[0]*p1[1]-p2[1]*p1[0])/float(p2[0]-p1[0])
        return [tan,y]
    else:
        return [999999.0,999999.0]

# cross
def cross(l1,l2):
    x = float(l1[1]-l2[1])/float(l2[0]-l1[0])
    return x

# cross in line
def cinline(x,x1,x2):
    check = 0
    if x>x1:
        check+=1
    if x>x2:
        check+=1
    if check==1:
        return 1
    return 0

# check that triangle contains origin
def orintri(tri):
    # line equation for each side
    l = []
    l.append(lequ(tri[2],tri[1]))
    l.append(lequ(tri[2],tri[0]))
    l.append(lequ(tri[0],tri[1]))

    # line equation for origin and each vertex
    lo = []
    lo.append(lequ(tri[0],[0,0]))
    lo.append(lequ(tri[1],[0,0]))
    lo.append(lequ(tri[2],[0,0]))

    # check
    check = 0
    for i in range(3):
        if l[i][0]!=999999.0:
            x = cross(l[i],lo[i])
            check+=cinline(x,tri[(i+1)%3][0],tri[(i+2)%3][0])
        else:
            check+=cinline(0,tri[(i+1)%3][1],tri[(i+2)%3][1])

    if check==3:
        return 1
    else:
        return 0

# read file
f = file('triangles.txt')
tri = []
for line in f:
    line = line.strip('\n')
    temp = line.split(',')
    tri.append([[int(temp[0]),int(temp[1])],[int(temp[2]),int(temp[3])],[int(temp[4]),int(temp[5])]])

res = 0
for i in range(len(tri)):
    res+=orintri(tri[i])

print res
