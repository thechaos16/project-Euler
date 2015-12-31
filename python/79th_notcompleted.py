import numpy as np

## check if the string contains target
def longestInclusion(string,target):
    if len(string)<len(target):
        return 0
    if len(target)==1:
        if target in string:
            return 1
        else:
            return 0
    i=0
    for char in target:
        check = 0
        while True:
            try:
                if string[i]==char:
                    check = 1
                    break
            except IndexError:
                check = 0
                break
            i+=1
        if check==0:
            break
    if check==1:
        return len(target)
    else:
        ## all strings with length for target-1
        maxtt = 0
        for j in range(len(target)):
            tt = longestInclusion(string,target[:j]+target[j+1:])
            if tt==len(target)-1:
                return tt
            if tt>=maxtt:
                maxtt = tt
        return maxtt

## generate new string which contains target
def addStr(string,target):
    ## check if string contains target
    strLen = longestInclusion(string,target)
    if strLen==len(target):
        return string
    return string

## find shortest for n data
def shortestStrings(keys):
    if len(keys)==1:
        return keys
    else:
        stringCand = shortestStrings(keys[:-1])
        newStringCand = []
        minStrLength = np.inf
        for string in stringCand:
            newString = addStr(string,keys[-1])
            newStringLen = len(newString)
            if newStringLen==minStrLength:
                newStringCand.append(newString)
            elif newStringLen<minStrLength:
                newStringCand = [newString]
                minStrLength = newStringLen
        return newStringCand



f = open('./keylog.txt','r')
keys = []

for line in f:
        line = line.strip('\n')
        keys.append(line)