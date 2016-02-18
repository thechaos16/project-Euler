# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 14:04:13 2016

@author: minkyu
"""

#import numpy as np

def find_repunit_less_than(a,n):
    res = []
    val = 1+a
    i=2
    while True:
        val+=a**i
        if val>n:
            break
        res.append(val)
        i+=1
    return res
    
def repunit_list_less_than(n):
    res = [1]
    i=2
    while True:
        tempRes = find_repunit_less_than(i,n)
        if len(tempRes)==0:
            break
        res+=tempRes
        res = list(set(res))
        i+=1
    return res
    
repun = repunit_list_less_than(10**12)
final_res = sum(repun)