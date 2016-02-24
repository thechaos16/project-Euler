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
    while True:
        if i>10e7:
            break
        [result,prev_fact_num] = check_factor_number(i,prev_fact_num)
        if result:
            #print(i)
            cnt+=1            
        i+=1
    return cnt
    
def check_factor_number(n,prev_fact_num=None):
    if n==1:
        return False
    if prev_fact_num is None:
        prev_fact_num = factor_number(n-1)
    cur_fact_num = factor_number(n)
    return [cur_fact_num==prev_fact_num,cur_fact_num]
        
def factor_number(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    factorization = factor.factorization(n)
    ans = 1.0
    for key in list(factorization):
        ans*=(factorization[key]+1)
    return ans
    
if __name__=='__main__':
    print(run())