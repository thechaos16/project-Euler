cubes = []

def radix(n):
    r=1
    while 'true':
        n/=10
        if n==0:
            break
        r+=1
    return r

def cube(n):
    a = n*n*n
    r = radix(a)
    if r<=len(cubes):
        if a not in cubes[r-1]:
            cubes[r-1].append(a)
    else:
        l=[a]
        cubes.append(l)
    #return a

def perm(a,b):
    la = []
    lb = []
    r = radix(a)
    for i in range(r):
        la.append(a%10)
        lb.append(b%10)
        a/=10
        b/=10
    la.sort()
    lb.sort()
    if la==lb:
        return 1
    return 0


for i in range(1,10000):
    cube(i)
    
for i in range(len(cubes)):
    for j in range(len(cubes[i])):
        cnt=1
        for k in range(len(cubes[i])):
            if j!=k:
                if perm(cubes[i][j],cubes[i][k])==1:
                    cnt+=1
        if cnt>=5:
            print cubes[i][j]

