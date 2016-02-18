# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 15:21:22 2016

@author: minkyu
"""

import numpy as np

class NumberMind:
    def __init__(self,n,result):
        self.radix = n
        ## sort result
        self.result = sorted(result,key=lambda x:x[1])
        ## initial candidate (array of set)
        self.candidate = [set(np.linspace(0,9,10))]*self.radix
        
    def update_candidate(self,rule):
        pass
        

def run():
    res = [[90342,2],[70794,0],[39458,2],[34109,1],[51545,2],[12531,1]]
    nmi = NumberMind(5,res)
    return nmi