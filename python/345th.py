# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 10:24:21 2016

@author: minkyu
"""

import numpy as np
import scipy as sci

class problem345:
    def __init__(self,inputMat):
        if type(inputMat)==str:
            self.inputMat = self.matrixParser(inputMat)
        else:
            self.inputMat = inputMat
        self.memo = {}

    def matrixParser(self,string):
        mat = []
        rows = string.split('\n')
        for row in rows:
            row = row.replace('   ',' ')
            row = row.replace('  ',' ')
            row = row.strip(' ')
            column = row.split(' ')
            #print(column)
            column = [int(elem) for elem in column]
            mat.append(column)
        return mat
        
    def findBestRes(self,mat):
        if len(mat)==1:
            return mat[0][0]
            
        matStr = self.matCoder(mat)
        if matStr in list(self.memo):
            return self.memo[matStr]
        
        maxRes = -np.inf
        for i in range(len(mat)):
            tempMat = sci.delete(mat,i,1)
            tempRes = mat[0][i]+self.findBestRes(sci.delete(tempMat,0,0))
            if tempRes>=maxRes:
                maxRes = tempRes
            
        self.memo[matStr] = maxRes
        return maxRes
        
    def matCoder(self,mat):
        matStr = ','.join([str(elm) for elm in mat])
        return matStr
        
      
      
inputStr = '  7  53 183 439 863 497 383 563  79 973 287  63 343 169 583\n627 343 773 959 943 767 473 103 699 303 957 703 583 639 913\n447 283 463  29  23 487 463 993 119 883 327 493 423 159 743\n217 623   3 399 853 407 103 983  89 463 290 516 212 462 350\n960 376 682 962 300 780 486 502 912 800 250 346 172 812 350\n870 456 192 162 593 473 915  45 989 873 823 965 425 329 803\n973 965 905 919 133 673 665 235 509 613 673 815 165 992 326\n322 148 972 962 286 255 941 541 265 323 925 281 601  95 973\n445 721  11 525 473  65 511 164 138 672  18 428 154 448 848\n414 456 310 312 798 104 566 520 302 248 694 976 430 392 198\n184 829 373 181 631 101 969 613 840 740 778 458 284 760 390\n821 461 843 513  17 901 711 993 293 157 274  94 192 156 574\n 34 124   4 878 450 476 712 914 838 669 875 299 823 329 699\n815 559 813 459 522 788 168 586 966 232 308 833 251 631 107\n813 883 451 509 615  77 281 613 459 205 380 274 302  35 805'
sampleMat = np.array([[7, 53, 183, 439, 863],[497, 383, 563,  79, 973],[287,63,343,169,583],[627,343,773,959,943],[767,473,103,699,303]])
instance = problem345(inputStr)
#instance = problem345(sampleMat)
res = instance.findBestRes(instance.inputMat)