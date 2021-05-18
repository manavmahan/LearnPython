#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 15:18:06 2021

@author: mahan
"""

def get_change_methods_dp(coin_set = [1,2,3,5], amount = 15):
    ar_change_methods = [list([0 for j in range (amount + 1)]) for i in range(len(coin_set) +1)]
    
    for i in range(len(coin_set) +1): ar_change_methods[i][0] = 1   
    for j in range(1, amount + 1): ar_change_methods[0][j] = 0
    
    for i in range(1, len(coin_set) + 1):
        for j in range(1, amount + 1):
            ar_change_methods[i][j] = ar_change_methods[i-1][j] if coin_set[i-1]>j else ar_change_methods [i-1][j] + ar_change_methods[i][j-coin_set[i-1]]
    
    return ar_change_methods[len(coin_set)][amount]

def get_change_methods_re(coin_set = [1,2,3,5], amount = 15):
    # solved
    if amount == 0: return 1
    
    # no solution
    if amount < 0 or (len(coin_set) == 0 and amount > 0): return 0
    
    #partial solutions
    #   1. remove a coin
    #   2. add a coin
    return get_change_methods_re(coin_set[:-1], amount) + get_change_methods_re(coin_set, amount - coin_set[-1])

a = get_change_methods_dp()
print(a)

def ways(candidates, target, sol = [], solutions = []):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    
    if target == 0:
        print(sol)
        solutions += [sol]
        return True
    
    if target < 0:
        return False
    
    if len(candidates) == 0 and target > 0:
        return False
    
    
    return ways(candidates[1:], target, sol, solutions) + ways(candidates, target - candidates[0], sol + [candidates[0]], solutions)