import math

def perm(a,b):
    a = str(a)
    b = str(b)
    if len(a)!=len(b):
        return 0
    l1 = []
    l2 = []
    for i in range(len(a)):
        l1.append(a[i])
        l2.append(b[i])
    l1.sort()
    l2.sort()
    if l1==l2:
        return 1
    return 0

def relapri(a,b):
    x,y=max(a,b),min(a,b)
    while 1:
        temp = x
        x = y
        y = temp%y
        if x==1:
            return 1
        if y==0:
            return 0

def euler(n):
    cnt=1
    for i in range(2,n):
        if relapri(i,n)==1:
            cnt+=1
    return cnt

minimum = 1.2
ans = 0
for i in range(1,1000000):
    temp = euler(i)
    if perm(i,temp)==1:
        if float(i)/float(temp)<minimum:
            minimum = float(i)/float(temp)
            ans = i

print ans
