# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 11:06:17 2015

@author: minkyu
"""
import time

def reduceProp(n):
    setCand = set(range(1,n))
    for i in setCand:
        if i==1:
            continue
        if n%i==0:
            divI = int(n/i)
            for j in range(1,divI):
                setCand = setCand-{j*i}
    return len(setCand)
    
start = time.clock()
res = 0
for i in range(2,10000):
    res+=reduceProp(i)
end = time.clock()
print(res)
print(end-start)