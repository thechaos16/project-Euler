# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 13:23:35 2016

@author: minkyu
"""

import sys
try:
    import modules.factorization as factor
except ImportError:
    sys.path.append('../')    
    import modules.factorization as factor

def run():
    cnt = 0
    i=2
    prev_fact_num = None
    factor_dict = {}
    while True:
        if i>10e7:
            break
        [result,prev_fact_num,factor_dict] = check_factor_number(i,prev_fact_num,factor_dict)
        if result:
            #print(i)
            cnt+=1            
        i+=1
    return cnt
    
def check_factor_number(n,prev_fact_num=None,factor_dict = {}):
    if n==1:
        return [False,factor_dict]
    if prev_fact_num is None:
        [prev_fact_num,factor_dict] = factor_number(n-1,factor_dict)
    [cur_fact_num,factor_dict] = factor_number(n,factor_dict)
    return [cur_fact_num==prev_fact_num,cur_fact_num,factor_dict]
        
def factor_number(n,factor_dict):
    if n<=0:
        return [0,factor_dict]
    elif n==1:
        return [1,factor_dict]
    [factorization,factor_dict] = factor.factorization(n,factor_dict)
    ans = 1.0
    for key in list(factorization):
        ans*=(factorization[key]+1)
    return [ans,factor_dict]
    
if __name__=='__main__':
    print(run())