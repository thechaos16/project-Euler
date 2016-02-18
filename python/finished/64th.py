import math

snumber = []

def pattern(l1,l2,l3):
    if len(l1)==1:
        return 0
    for i in range(len(l1)-1):
        if l1[i]==l1[len(l1)-1] and l2[i]==l2[len(l2)-1] and l3[i]==l3[len(l3)-1]:
            return len(l1)-i-1
    return 0

def period(n):
    a0 = int(math.sqrt(n))
    b0 = int(math.sqrt(n))
    c0 = 1
    aseries = []
    bseries = []
    cseries = []
    while(1):
        tempa = int(c0/(math.sqrt(n)-b0))
        aseries.append(tempa)
        tempc = (n-b0*b0)/c0
        tempb = -(b0-tempa*(n-b0*b0)/c0)
        bseries.append(tempb)
        cseries.append(tempc)
        c0 = tempc
        b0 = tempb
        kk = pattern(aseries,bseries,cseries)
        if kk!=0:
            return kk             
    return n

for i in range(101):
    snumber.append(i*i)

result = []
odd = []

for i in range(2,10000):
    if i in snumber:
        continue
    temp = period(i)
    if temp%2==1:
        odd.append(temp)
    result.append(temp)
