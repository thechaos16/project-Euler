# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 17:37:39 2016

@author: minkyu
"""

def equ(a,b):
    return (a-b)*(a+b-1)-b*(b-1)
    
def is_equ(n):
    for i in range(int(0.25*n),n):
        temp_res = equ(n,n-i)
        if temp_res==0:
            return [n,n-i]
        elif temp_res>0:
            return None

def run():
    i = 10**12
    
    while True:
        if is_equ(i) is not None:
            print(i)
            break
        i+=1
    return i