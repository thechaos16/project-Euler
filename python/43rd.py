import math

def char(n,pri):
    n = str(n)
    check=1
    for i in range(1,8):
        temp = int(n[i:i+3])
        if temp%pri[i-1]!=0:
            check=0
            break
    return check

def prime(n):
    check=1
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            check=0
            break
    return check

def pand(l):
    if len(l)==1:
        return [l]
    ans = []
    for i in range(len(l)):
        asdf=[]
        for j in range(len(l)):
            if l[j]!=l[i]:
                asdf.append(l[j])
        temp = pand(asdf)
        for j in range(len(temp)):
            temp[j].append(l[i])
            ans.append(temp[j])
    return ans

def ltoi(l):
    ans=0
    for i in range(len(l)):
        ans+=l[i]*pow(10,len(l)-i-1)
    return ans

pri = []
for i in range(2,20):
    if prime(i)==1:
        pri.append(i)
pandset = pand([1,2,3,4,5,6,7,8,9,0])
ans = []
cnt=0
for i in range(len(pandset)):
    if char(ltoi(pandset[i]),pri)==1:
        ans.append(pandset[i])
        cnt+=ltoi(pandset[i])
    
