# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 15:21:22 2016

@author: minkyu
"""

import numpy as np

class NumberMind:
    def __init__(self, n, result):
        self.radix = n
        ## sort result
        self.result = sorted(result,key=lambda x:x[1])
        ## initial candidate (array of set)
        self.candidate = []
        for i in range(self.radix):
            self.candidate.append(set(np.array(np.linspace(0,9,10, dtype=int), dtype=str)))
        
    def find_answer(self):
        for rule in self.result:
            self.update_candidate(rule)
        try:
            return self.convert_answer_from_candidates()
        except ValueError as e:
            raise ValueError(e)
    
    def convert_answer_from_candidates(self):
        answer = ''
        for cand_set in self.candidate:
            if len(cand_set) != 1:
                raise ValueError('Candidate should be only 1!')
            answer += str(int(list(cand_set)[0]))
        return answer
        
    def update_candidate(self, rule):
        # remove zero matches
        if rule[1] == 0:
            str_number = str(rule[0])
            for i in range(self.radix):
                print(str_number[i])
                self.candidate[i] -= set([str_number[i]])
        

def run():
    res = [(90342,2),(70794,0),(39458,2),(34109,1),(51545,2),(12531,1)]
    nmi = NumberMind(5,res)
    try:
        return nmi.find_answer
    except ValueError as e:
        print(e)
        return False


if __name__ == '__main__':
    res = [(90342,2),(70794,0),(39458,2),(34109,1),(51545,2),(12531,1)]
    nmi = NumberMind(5,res)
    