# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 10:56:07 2016

@author: minkyu
"""

import numpy as np

def is_palindrome(number):
    num_str = str(int(number))
    num_reverse = num_str[::-1]
    return num_str==num_reverse

def sum_of_consecutive_squares(n):
    limit = int(np.sqrt(n))
    print(limit)
    return_list = []
    for i in range(1,limit+1):
        for j in range(1,i+1):
            temp_num = np.sum([elm**2 for elm in range(1,limit-i+1)])
            return_list.append(temp_num)
    return return_list

if __name__=='__main__':
    aa = sum_of_consecutive_squares(10)
    print(aa)