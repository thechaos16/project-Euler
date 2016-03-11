# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 11:45:37 2016

@author: minkyu
"""
import numpy as np
import pandas as pd

def distance_calculator(coord1,coord2,radius):
    dot_proudct = np.dot(np.array(coord1),np.array(coord2))
    cos_theta = dot_proudct/(radius**2)
    return np.arccos(cos_theta)

def find_valid_coord(radius):
    all_candidates = cartesian2([np.arange(-radius,radius+1,1)]*3)
    valid_set = []
    for cand in all_candidates:
        if np.sum(np.array(cand)**2)==radius**2:
            valid_set.append(cand)
    return valid_set

def find_minimum_risk_way(start,destination,distance_map,dictionary_coord):
    start_idx = dictionary_coord[','.join([str(elm) for elm in start])]
    destination_idx = dictionary_coord[','.join([str(elm) for elm in destination])]
    
    return (distance_map[start_idx][destination_idx]/np.pi)**2
        
def cartesian2(arrays):
    arrays = [np.asarray(a) for a in arrays]
    shape = (len(x) for x in arrays)

    ix = np.indices(shape, dtype=int)
    ix = ix.reshape(len(arrays), -1).T

    for n, arr in enumerate(arrays):
        ix[:, n] = arrays[n][ix[:, n]]

    return ix

def run(radius):
    coord_set = find_valid_coord(radius)
    distance_map = np.zeros((len(coord_set),len(coord_set)))
    dictionary_coord = {}
    for i in range(len(coord_set)):
        for j in range(len(coord_set)):
            if i==0:
                dictionary_coord[','.join([str(elm) for elm in coord_set[j]])] = j
            if i==j:
                continue
            theta = distance_calculator(coord_set[i],coord_set[j],radius)
            #distance = radius*theta
            distance_map[i][j] = theta
            distance_map[j][i] = theta
    #return distance_frame
    min_risk = find_minimum_risk_way([0,0,radius],[0,0,-radius],distance_map,dictionary_coord)
    return min_risk
    

if __name__=='__main__':
    r = 7
    res = run(r)