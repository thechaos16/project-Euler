# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 10:39:54 2016

@author: minkyu
"""

import sys
import numpy as np


def is_squre(n):
    return int(np.sqrt(n)) == np.sqrt(n)


def number_of_lattice(a, b, c, d):
    if a < 1 or b < 1 or c > -1 or d > -1:
        sys.exit('Error!')
    # full rectangle
    full_rectangle = (a - c + 1) * (b - d + 1)
    return int((full_rectangle + 1) / 2)


def run():
    m = 4
    cnt = 0
    all_number = 0
    for a in range(1, m + 1):
        for b in range(1, m + 1):
            for c in range(1, m + 1):
                for d in range(1, m + 1):
                    lattice = number_of_lattice(a, b, -c, -d)
                    all_number += 1
                    if is_squre(lattice):
                        cnt += 1
    return cnt
