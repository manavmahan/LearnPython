#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 17:29:48 2021

@author: mahan
"""

import numpy as np

    
def is_safe(x, y, n, board):
    '''
    is inside the board (non-negative and less than n) and empty square
    '''
    return x>=0 and y>=0 and x<n and y<n and board[x, y] == 0

def solve(n, board, moves, curr_x, curr_y):
    # solution found
    if moves == 60:
        return True
    
    move_x = [1, 2, -1, -2,  2,  1, -1, -2]
    move_y = [2, 1,  2,  1, -1, -2, -2, -1]
    
    # all the possibilities
    for i in range(8):        
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]        
        
        # is possible move
        if is_safe(new_x, new_y, n, board):        
            board[new_x, new_y] = moves + 1    
            
            # recursion if part of solution
            if solve(n, board, moves + 1, new_x, new_y):
                return True        
            
            #back track
            board[new_x, new_y] = 0
    return False
    
def solver():
    n = 8
    board = np.zeros([n,n])
    
    board[3,0] = 1
    
    solve(n, board, 1, 0, 0)
    
    print (board)
    
solver()