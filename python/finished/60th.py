import math

pri = [2,3,5]

def prime(n):
    if n in pri:
        return 1
    for i in range(2,math.sqrt(n)+1):
        if n%i==0:
            return 0
    pri.append(n)
    return 1

def radix(n):
    r=1
    while 'true':
        n/=10
        if n==0:
            break
        r+=1
    return r

def concat2(a,b):
    r1 = radix(a)
    r2 = radix(b)
    if prime(a*math.pow(10,r2)+b)==1 and prime(b*math.pow(10,r1)+a)==1:
        return 1
    return 0

for i in range(2,10000):
    prime(i)

con = []
pp = len(pri)
for a in range(pp-4):
    for b in range(a+1,pp-3):
        if concat2(pri[a],pri[b])==1:
            for c in range(b+1,pp-2):
                if concat2(pri[a],pri[c])==1 and concat2(pri[b],pri[c])==1:
                    for d in range(c+1,pp-1):
                        if concat2(pri[a],pri[d])==1 and concat2(pri[b],pri[d])==1 and concat2(pri[c],pri[d])==1:
                            for e in range(d+1,pp):
                                if concat2(pri[a],pri[e])==1 and concat2(pri[b],pri[e])==1 and concat2(pri[c],pri[e])==1 and concat2(pri[d],pri[e])==1:
                                    con.append([pri[a],pri[b],pri[c],pri[d],pri[e]])
