import math

pri = [2,3,5,7,11,13];

def isprime(n):
    if n in pri:
        return 1
    for i in range(len(pri)):
        if n%pri[i]==0:
            return 0
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return 0
    pri.append(n)
    return 1

def divisors(n):
    div = []
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            if i not in div:
                div.append(i+n/i)
    return div

def checker(n):
    div = divisors(n)
    dd=0
    for i in range(len(div)):
        if isprime(div[i])==0:
            dd=1
            break
    if dd==0:
        return 1
    return 0

nn = []
for i in range(2,100000000):
    if checker(i)==1:
        nn.append(i)

        
