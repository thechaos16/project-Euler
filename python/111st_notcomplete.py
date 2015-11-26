import os,sys
import math

prime = [2]
digits = [0,1,2,3,4,5,6,7,8,9]

# return combination (0~n-1)
def comb(n,r):
    res = []
    check = 0
    if r==0:
        return [[]]
    elif r==n:
        return [range(n)]
    else:
        if r>n/2:
            r = n-r
            check = 1
        kk = comb(n,r-1)
        for i in range(len(kk)):
            for j in range(n):
                if j not in kk[i]:
                    temp = kk[i]+[j]
                    temp.sort()
                    if check==0:
                        if temp not in res:
                            res.append(temp)
                    else:
                        temp2 = range(n)
                        for k in range(len(temp)):
                            temp2.remove(temp[k])
                        if temp2 not in res:
                            res.append(temp2)
    return res

# set prime less than n
def setprime(n):
    for i in range(2,n):
        temp = isprime(i)
    f = file('prime.txt','w')
    for i in range(len(prime)):
        f.write(str(prime[i]))
        f.write('\n')
    f.close()

# read prime.txt
def defprime():
    f = file('prime.txt','r')
    for line in f:
        temp = line.strip('\n')
        if int(temp) not in prime:
            prime.append(int(temp))
        

# check if there is a prime
def isprime(n):
    if n in prime:
        return 1
    if n<=prime[len(prime)-1]:
        return 0
    for i in range(2,n/2+1):
        if n%i==0:
            return 0
    prime.append(n)
    prime.sort()
    return 1

# convert list to integer
def ltoi(l):
    temp = ''
    for i in range(len(l)):
        temp+=l[i]
    return int(temp)

# define set
def slist(d,sol):
    res = [[]]
    for i in range(sol):
        tempres = []
        for j in range(len(res)):
            for k in range(10):
                if k!=d:
                    temp = res[j]+[str(k)]
                    tempres.append(temp)
        res = []
        for j in range(len(tempres)):
            res.append(tempres[j])
    return res

# get candidates for prime
def candidate(l,n,d):
    res = []
    temp = []
    for i in range(n):
        temp.append(str(d))
    for i in range(len(l)):
        temp2 = slist(d,len(l[i]))
        for j in range(len(temp2)):
            for kk in range(len(l[i])):
                temp[l[i][kk]] = temp2[j][kk]
            if temp[0]!='0':
                temp3 = ltoi(temp)
                res.append(temp3)
            for kk in range(len(l[i])):
                temp[l[i][kk]] = str(d)
    return res

def finres(num,d):
    m = -1
    n = 0
    s = 0
    for i in range(num):
        temp = num-i
        tempcomb = comb(num,i)
        res = candidate(tempcomb,num,d)
        for j in range(len(res)):
            if isprime(res[j])==1:
                m = temp
                n+=1
                s+=res[j]
        if m!=-1:
            break
        n = 0
        s = 0
    return [m,n,s]

ans = []
n = 10
#n = 4
defprime()
#setprime(int(math.pow(10,n+1)))
for i in range(10):
    ans.append(finres(n,i))
