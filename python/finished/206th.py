# -*- coding: utf-8 -*-

import re

def checker(num):
    targetStr = r'1\d2\d+3\d+4\d+5\d+6\d+7\d+8\d+9'
    return re.match(targetStr,str(num))
    
for i in range(5000000):
    check = 0
    for j in range(2):
        betweenStr = str(i)
        strLen = len(betweenStr)
        if strLen!=7:
            for k in range(7-strLen):
                betweenStr = '0'+betweenStr
        if j==0:
            newNum = int('1'+betweenStr+'3')
        else:
            newNum = int('1'+betweenStr+'7')
        #print(newNum)
        if checker((newNum)**2):
            check=1
    if check==1:
        print(i)
        break
        