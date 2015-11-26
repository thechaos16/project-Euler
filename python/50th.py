import math

pri = [2,3,5]

def prime(n):
    if n in pri:
        return 1
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return 0
    pri.append(n)
    return 1

for i in range(6,1000000):
    k = prime(i)

ans=0
i=0
a=0
while 'true':
    while 'true':
        ans+=pri[a+i]
        if ans>=1000000:
            ans-=pri[a+i]
            break
        i=i+1
    if prime(ans)==1:
        print ans
        print i-a
        break
    a+=1
    ans=0
    i=0
