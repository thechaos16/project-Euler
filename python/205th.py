# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 11:20:19 2016

@author: minkyu
"""

import numpy as np

class DiceProbability:
    def __init__(self,number_of_dice,max_number):
        self.number_of_dice = number_of_dice
        self.max_number = max_number
        self.probability_map = self.compute_map()
        
    def get_probability(self,target_sum):
        real_idx = target_sum-self.number_of_dice
        if real_idx<0 or real_idx>len(self.probability_map):
            print(str(target_sum) + ' is impossible!')
            return 0
        return self.probability_map[real_idx]
    
    ## it should be in the form of fractional number
    def compute_map(self):
        number_of_entire_cases = self.max_number**self.number_of_dice
        case_interval = [self.number_of_dice,self.number_of_dice*self.max_number]      
        probability_map = np.zeros(case_interval[1]-case_interval[0]+1)
        for i in range(number_of_entire_cases):
            decimal_num = self.n_decimal_number(i,self.max_number,self.number_of_dice)
            result_sum = np.sum([int(elm)+1 for elm in decimal_num])
            probability_map[result_sum-self.number_of_dice]+=1
        probability_map = [str(elm)+'/'+str(number_of_entire_cases) for elm in probability_map]
        return probability_map
        
    def n_decimal_number(self,target,n,radix):
        result_str = ''
        while True:
            if target<n:
                result_str = str(target)+result_str
                if len(result_str)!=radix:
                    result_str = '0'*(radix-len(result_str))+result_str
                return result_str
            residual = target%n
            result_str = str(residual)+result_str
            target = int(target/n)
        
if __name__=='__main__':
    peter = DiceProbability(9,4)
    colin = DiceProbability(6,6)
    prob_res = 0.0
    for i in range(36,8,-1):
        temp_result = eval(peter.get_probability(i))*(1-np.sum([eval(colin.get_probability(elm)) for elm in range(i,37)]))
        prob_res+=temp_result
    print(prob_res)