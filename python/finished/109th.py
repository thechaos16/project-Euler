import os,sys
import math

dart = [20,1,18,4,13,6,10,15,2,17,3,19,7,16,8,11,14,9,12,5,25]
buff = ['S','D','T']

# 1 or 2 element to make n
def check(n):
    if n==0:
        return ['']
    res=[]
    # single element
    for i in range(len(dart)):
        if n==dart[i]:
            res.append(buff[0]+str(n))
        if n==2*dart[i]:
            res.append(buff[1]+str(dart[i]))
        if n==3*dart[i]:
            if dart[i]==25:
                continue
            res.append(buff[2]+str(dart[i]))
    # two elements
    # Single/Single or Double or Triple
    for i in range(len(dart)):
        if n<=dart[i]:
            continue
        newn = n-dart[i]
        temp = buff[0]+str(dart[i])
        # single
        for j in range(i,len(dart)):
            if newn==dart[j]:
                res.append(temp+buff[0]+str(dart[j]))
        # double
        for j in range(len(dart)):
            if newn==dart[j]*2:
                res.append(temp+buff[1]+str(dart[j]))
        # triple
        for j in range(len(dart)):
            if newn==dart[j]*3:
                if dart[j]==25:
                    continue
                res.append(temp+buff[2]+str(dart[j]))            
    # Double/Double or Triple
    for i in range(len(dart)):
        if n<=2*dart[i]:
            continue
        newn = n-2*dart[i]
        temp = buff[1]+str(dart[i])
        # double
        for j in range(i,len(dart)):
            if newn==dart[j]*2:
                res.append(temp+buff[1]+str(dart[j]))
        # triple
        for j in range(len(dart)):
            if newn==dart[j]*3:
                if dart[j]==25:
                    continue
                res.append(temp+buff[2]+str(dart[j]))
    # Triple/Triple
    for i in range(len(dart)):
        if n<=3*dart[i]:
            continue
        if dart[i]==25:
            continue
        newn = n-3*dart[i]
        temp = buff[2]+str(dart[i])
        # triple
        for j in range(i,len(dart)):
            if newn==dart[j]*3:
                if dart[j]==25:
                    continue
                res.append(temp+buff[2]+str(dart[j]))    
    return res

# number of checkout for target n
def checkout(n):
    ans = []
    for i in range(len(dart)):
        if dart[i]*2>n:
            continue
        temp = buff[1]+str(dart[i])
        temp2 = n-2*dart[i]
        res = check(temp2)
        for j in range(len(res)):
            temp3 = temp+res[j]
            ans.append(temp3)
    return ans

res = []
cnt = 0
for i in range(2,100):
    temp = checkout(i)
    cnt+=len(temp)
