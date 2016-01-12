import math

def isprime(n,pri):
    if n in pri:
        return 1
    for i in range(len(pri)):
        if n%pri[i]==0:
            return 0
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return 0
    #pri.append(n)
    return 1

def primeLessThan(n):
    #priList = [2]
    priList = []
    for i in range(2,n+1):
        if isprime(i,priList):
            priList.append(i)
    return priList

def divisors(n):
    div = []
    for i in range(1,int(math.sqrt(n))+1):
        if n%i==0:
            if i not in div:
                div.append(i+n/i)
    return div

def checker(n,priList):
    div = divisors(n)
    dd=0
    for i in range(len(div)):
        if isprime(div[i],priList)==0:
            dd=1
            break
    if dd==0:
        return 1
    return 0

nn = []
#for i in range(2,100000000):
 #   if checker(i)==1:
  #      nn.append(i)

priList = primeLessThan(100000000)
print('list is finished')
cnt=0
for prime in priList:
    if checker(prime-1,priList):
        #print(prime-1)
        cnt+=prime-1
