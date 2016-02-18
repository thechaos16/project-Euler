import math

def penta(n):
    return n*(3*n-1)/2

def ispenta(k):
    n = 1+math.sqrt(1+24*k)
    n = n/6
    if n-int(n)==0:
        return int(n)
    else:
        return 0


for i in range(1,10000):
    for j in range(i,10000):
        if ispenta(penta(j)-penta(i))!=0 and ispenta(penta(i)+penta(j))!=0:
            print penta(j)-penta(i)
            break

