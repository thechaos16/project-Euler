# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 13:30:32 2016

@author: minkyu
"""

import sys
try:
    import modules.prime_handler as ph
except ImportError:
    sys.path.append('../')
    import modules.prime_handler as ph

def update_factor_dictionary(prev_dict,new_dict):
    keys = list(new_dict)
    for key in keys:
        if key not in prev_dict:
            prev_dict[key] = new_dict[key].copy()
    return prev_dict

def factorization(n,factor_dict={}):
    if int(n) in factor_dict:
        return [factor_dict[int(n)],factor_dict]
    phi = ph.PrimeHandler(n)
    prime_list = phi.get_prime_list()
    if n in prime_list:
        factor_dict = update_factor_dictionary(factor_dict,{int(n):{int(n):1}})
        return [{int(n):1},factor_dict]
    return_dict = {}
    for prime in prime_list:
        if n%prime==0:
            if int(n/prime) in factor_dict:
                return_dict = factor_dict[int(n/prime)].copy()
            else:
                [return_dict, new_factor_dict] = factorization(n/prime,factor_dict)
                factor_dict = update_factor_dictionary(factor_dict,new_factor_dict)
            if int(prime) in list(return_dict):
                return_dict[int(prime)]+=1
            else:
                return_dict[int(prime)]=1
            factor_dict[int(n)]=return_dict.copy()
            return [return_dict, factor_dict]
    
if __name__=='__main__':
    factor_dict = {}
    for i in range(2,10):
        [aa, factor_dict] = factorization(i,factor_dict)