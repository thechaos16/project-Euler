# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 17:02:02 2016

@author: minkyu
"""

## basic assumption a<=b<=c
## if the player wins, return True, otherwise, return False
def Nim(a,b,c):
    if a==b==c==0:
        return False
    if a==b==0:
        return True
        
    if a!=0:
        if not Nim(0,b,c):
            return True
        if a>1:
            if not Nim(1,b,c):
                return True
    
    for i in range(1,a+1):
        if not Nim(a-i,b,c):
            return True
            
    for i in range(1,b+1):
        ll = [a,b-i,c]
        ll.sort()
        if not Nim(ll[0],ll[1],ll[2]):
            return True
    
    for i in range(1,c+1):
        ll = [a,b,c-i]
        ll.sort()
        if not Nim(ll[0],ll[1],ll[2]):
            return True
            
    return False