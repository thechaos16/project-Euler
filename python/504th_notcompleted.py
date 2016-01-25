# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 10:39:54 2016

@author: minkyu
"""

import sys
import numpy as np

def isSquare(n):
    return int(np.sqrt(n))==np.sqrt(n)
    
def numLattice(a,b,c,d):
    if a<1 or b<1 or c>-1 or d>-1:
        sys.exit('Error!')
    ## full rectangle
    fullRec = (a-c+1)*(b-d+1)
    return int((fullRec+1)/2)

m=4
cnt= 0
allNum = 0
for a in range(1,m+1):
    for b in range(1,m+1):
        for c in range(1,m+1):
            for d in range(1,m+1):
                lattice = numLattice(a,b,-c,-d)
                allNum+=1
                if isSquare(lattice):
                    cnt+=1