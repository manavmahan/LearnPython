#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 20:15:09 2021

@author: mahan
"""
import numpy as np

def board_to_np(board):
    n = len(board[0])
    np_board = np.zeros([n, n])
    for r, row in enumerate(board):
        for c, col in enumerate(row):
            try:
                int(col)
            except:
                None
            else:
                np_board[r, c] = int(board[r][c])
    return np_board
    
def is_complete_seq(s):
    return 45==sum(s)

def min_poss_cell(board):
    search_array = 10 * np.ones(board.shape)
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row, col] == 0:
                vals = [a for a in range(1, 10) if is_safe(board, row, col, a)]
                if len(vals) == 1: 
                    return row, col
                search_array[row, col] = len(vals)
    min_cell = np.argmin(search_array)
    return min_cell//9, min_cell%9
    

def is_safe(board, row, col, v):
    if v in board[row, :]:
        return False
    if v in board[:, col]:
        return False
    r, c = row//3, col//3
    if v in board[r*3:r*3+3, c*3:c*3+3].flatten():
        return False
    return True
        
def solveSudoku(board):
    """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
    """
    # solving row-wise; marking the solution
    if all(is_complete_seq(board[a] for a in range(9))):
        print(board)
        return True
    
    row, col = min_poss_cell(board)

    # all possible solutions
    vals = [a for a in range(1, 10)]
    
    for v in vals:   
        #constraint
        if is_safe(board, row, col, v):
            #make change
            board[row, col] = v
            print(row, col, v, '\n', board)
            if solveSudoku(board):
                #return True in case of partial solution; otherwise backtrack
                return True
    
            #backtrack
            board[row, col] = 0
    return False

board = np.array(
            [[8, 2, 7, 0, 0, 0, 3, 9, 0],
             [9, 6, 5, 0, 2, 0, 1, 4, 0],
             [0, 4, 0, 0, 8, 0, 7, 0, 2],
             [0, 0, 3, 0, 0, 0, 2, 0, 0],
             [4, 7, 0, 5, 1, 0, 6, 0, 0],
             [6, 1, 0, 0, 7, 0, 4, 0, 0],
             [7, 8, 0, 2, 3, 0, 0, 1, 4],
             [1, 5, 0, 7, 0, 6, 0, 0, 3],
             [2, 3, 9, 8, 4, 1, 0, 6, 7]])

board = np.array([
    [ 5, 3, 4, 6, 7, 8, 9, 1, 2],
    [ 6, 0, 0, 1, 9, 5, 0, 0, 0], 
    [ 0, 9, 8, 0, 0, 0, 0, 6, 0], 
    [ 8, 0, 0, 0, 6, 0, 0, 0, 3], 
    [ 4, 0, 0, 8, 0, 3, 0, 0, 1], 
    [ 7, 0, 0, 0, 2, 0, 0, 0, 6], 
    [ 0, 6, 0, 0, 0, 0, 2, 8, 0], 
    [ 0, 0, 0, 4, 1, 9, 0, 0, 5], 
    [ 0, 0, 0, 0, 8, 0, 0, 7, 9]
    ])
valid_boards =[]
print(solveSudoku(board))
