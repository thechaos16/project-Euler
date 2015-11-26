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
        temp = d*y*y+1
        if sqrt(temp)==1:
            return pow(temp,0.5)
        y+=1

def ans(d1,d):
    x = -1
    res = 1
    for i in range(d1,d+1):
        tempx = dequ(i)
        if x<=tempx:
            x = tempx
            res = i
            print x, res
    return x, res
