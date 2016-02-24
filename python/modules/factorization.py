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
    

def factorization(n):
    phi = ph.PrimeHandler(n)
    prime_list = phi.get_prime_list()
    if n in prime_list:
        return {int(n):1}
    return_dict = {}
    for prime in prime_list:
        if n%prime==0:
            return_dict = factorization(n/prime)
            if int(prime) in list(return_dict):
                return_dict[int(prime)]+=1
            else:
                return_dict[int(prime)]=1
            return return_dict
    
if __name__=='__main__':
    print(factorization(14))