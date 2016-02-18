import os,sys
import math

def reciprocal(n):
    cnt = 0
    for i in range(n+1,n*2+1):
       if (n*i)%(i-n)==0:
           cnt+=1
    return cnt

i=1000
while 1:
    if reciprocal(i)>=1000:
        break
    i+=1
