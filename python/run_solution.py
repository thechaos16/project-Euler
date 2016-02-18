# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 13:42:20 2016

@author: minkyu
"""

import modules.prime_handler as ph
import importlib

if __name__=='__main__':
    filename = '66th'
    required_file = None
    run_sol = importlib.import_module('ongoing.'+filename)
    
    if required_file is None:
        result = run_sol.run()
    else:
        result = run_sol.run(required_file)