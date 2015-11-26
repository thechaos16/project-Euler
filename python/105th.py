import sys,os
import math

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

# subset (non-empty, non-identical)
def sset(data):
    res = []
    for i in range(1,len(data)):
        temp = comb(len(data),i)
        for j in range(len(temp)):
            temp2 = []
            for k in range(len(temp[j])):
                temp2.append(data[temp[j][k]])
            res.append(temp2)
    return res

# inverse set of subset
def others(data,sub):
    temp = []
    for i in range(len(data)):
        if data[i] not in sub:
            temp.append(data[i])
    return temp

# disjoint
def disjoint(s1,s2):
    for i in range(len(s1)):
        if s1[i] in s2:
            return 0
    return 1

# first condition
def fcond(data):
    subsets = sset(data)
    for i in range(len(subsets)):
        for j in range(i+1,len(subsets)):
            if disjoint(subsets[i],subsets[j])==1:
                if sum(subsets[j])==sum(subsets[i]):
                    return 0
    return 1

# second condition
def scond(data):
    subsets = sset(data)
    for i in range(len(subsets)):
        for j in range(i+1,len(subsets)):
            lb = len(subsets[i])
            lc = len(subsets[j])
            if lb==lc:
                continue
            if disjoint(subsets[i],subsets[j])==1:
                if lb>lc:
                    if sum(subsets[i])<=sum(subsets[j]):
                        return 0
                else:
                    if sum(subsets[i])>=sum(subsets[j]):
                        return 0
    return 1

# check if the set is special (0: not, 1: special)
def isspecial(data):
    temp = fcond(data)+scond(data)
    if temp==2:
        return 1
    return 0


# read file
f = file('p105_sets.txt','r')
db = []
for line in f:
    line = line.strip('\n')
    temp = line.split(',')
    for i in range(len(temp)):
        temp[i] = int(temp[i])
    temp.sort()
    db.append(temp)

# check
res = 0
for i in range(len(db)):
    if isspecial(db[i])==1:
        print i
        res+=sum(db[i])
