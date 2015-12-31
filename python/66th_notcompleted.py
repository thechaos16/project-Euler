import math

def sqrt(n):
    temp = pow(n,0.5)
    if temp==int(temp):
        return 1
    return 0


def dequ(d):
    y=1
    if sqrt(d)==1:
        return -1
    while(True):
        y = y%10000
        temp = d*y*y+1
        if sqrt(temp)==1:
            return [pow(temp,0.5),y]
        y+=1

def ans(d):
    x = -1
    for i in range(d+1):
        if sqrt(i)==1:
            continue
        [tempx, tempy] = dequ(i)
        if x<=tempx:
            x = tempx
            res = i
            print [x, res, tempy]
    return [x, res]

[x, res] = ans(1000)
