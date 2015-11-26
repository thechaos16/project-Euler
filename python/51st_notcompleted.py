import math
import itertools

pri = [2,3,5,7,11]

def prime(n):
    if n in pri:
        return 1
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return 0
    pri.append(n)
    return 1

def family(n,l):
    result = []
    for j in range(10):
        if j==0:
            if 0 in l:
                continue
        kk = ''
        for i in range(len(str(n))):
            if i in l:
                kk+=str(j)
            else:
                kk+=str(n)[i]
        result.append(int(kk))
    return result

def nop(n,l):
    kk = family(n,l)
    ans = 0
    for i in range(len(kk)):
        if prime(kk[i])==1:
            ans+=1
        if ans==9:
            break
    return ans
    
def index(n):
    radix = len(str(n))
    ans = []
    for i in range(1,radix+1):
        temp = list(itertools.combinations(range(radix),i))
        for j in range(len(temp)):
            if nop(n,temp[j])==9:
                ans = family(n,temp[j])
    return ans
            
i = 1000
while(True):
    temp = index(i)
    if len(temp)!=0:
        print temp
        break
    i+=1
