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


# disjoint
def disjoint(s1,s2):
    for i in range(len(s1)):
        if s1[i] in s2:
            return 0
    return 1

# skipper
def skip(s1,s2):
    check = 0
    for i in range(len(s1)):
        if s1[i]<s2[i]:
            check+=1
    if check==len(s1):
        return 1
    return 0

# first condition
def fcond(data):
    subsets = sset(data)
    cnt = 0
    for i in range(len(subsets)):
        for j in range(i+1,len(subsets)):
            # since second condition is satisfied basically
            if len(subsets[i])!=len(subsets[j]):
                continue
            # strictly increasing, so subset contains only one element should not to be counted
            if len(subsets[i])==0 or len(subsets[i])==len(data) or len(subsets[i])==1:
                continue
            # largest element of one subset is smaller than smallest one of another
            if subsets[i][len(subsets[i])-1]<=subsets[j][0]:
                continue
            # if every element of one subset is smaller than matched one of another
            if skip(subsets[i],subsets[j])==1:
                continue
            if disjoint(subsets[i],subsets[j])==1:
                #print subsets[i]
                #print subsets[j]
                cnt+=1
    return cnt

a = [1,2,3,4,5,6,7,8,9,10,11,12]
#a = [1,2,3,4,5,6,7]
#a = [1,2,3,4]
#kk = fcond(a)
