# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 11:15:37 2016

@author: minkyu
"""

def is_step_number(n):
    prev_num = n%10
    n/=10
    while True:
        n = int(n)
        if n<10:
            break
        cur_num = n%10
        n/=10
        if abs(cur_num-prev_num)!=1:
            return False
        prev_num = cur_num
    return True
    
def is_pandigital_number(n):
    keys = set(str(n))
    if len(keys)==9:
        return True
    return False

def run():  
    aa = 10e8
    limit = 10e40
