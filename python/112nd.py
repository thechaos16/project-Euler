# -*- coding: utf-8 -*-

def isIncreasing(num):
    numStr = str(num)
    for i in range(len(numStr)-1):
        if int(numStr[i+1])-int(numStr[i])<0:
            return False
    return True
    
def isDecreasing(num):
    numStr = str(num)
    for i in range(len(numStr)-1):
        if int(numStr[i])-int(numStr[i+1])<0:
            return False
    return True

def isBouncy(num):
    if not isIncreasing(num) and not isDecreasing(num):
        return True
    return False
    
i=1000001
BouncyNum = 987048

while True:
    if isBouncy(i):
        #print(i)
        BouncyNum+=1
    if float(BouncyNum/i)>=0.99:
        break
    if i>=100000000:
        break
    i+=1