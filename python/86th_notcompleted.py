import math

def pyth(n):
        for i in range(1,n):
                for j in range(1,n):
                        if i*i+j*j==n*n:
                                return [i,j]
        return [-1,-1]

def mostpyth(n):
        temp = n
        while(1):
                li = pyth(temp)
                if li[0]==-1:
                        temp-=1
                        continue
                return [li[0],li[1],temp]

def gcd(a,b):
        for i in range(2,a+1):
                if a%i==0 and b%i==0:
                        return i
        return 1

def findpyth(n):
        temp = n
        while(1):
                li = pyth(temp)
                if li[0]!=-1:
                        if gcd(li[0],li[1])==1:
                                print [li[0],li[1],temp]
                temp-=1
                if temp<2:
                        break
        return 0
