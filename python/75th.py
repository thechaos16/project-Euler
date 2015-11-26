import math

storage = []
over2 = []

def tri(a,b,c):
    if a*a+b*b==c*c:
        return 1
    else:
        return 0

def onetri(n):
    check = 0
    kk = 0
    for i in range(len(over2)):
        if n%storage[i]==0:
            return 0
    
    for i in range(len(storage)):
        if n%storage[i]==0:
            check+=1
            kk=1
            if check==2:
                over2.append(n)
                return 0

    check = 0

    # need to be optimized
    for i in range(1,n/3):
        for j in range(i+1,n/2):
            if tri(i,j,n-i-j)==1:
                check+=1
                if check==2:
                    over2.append(n)
                    return 0

                
    if check==1:
        if kk==0:
            storage.append(n)
        return 1
    else:
        return 0

ans = 0

for i in range(12,1500000):
    if onetri(i)==1:
        ans+=1
