#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 16:18:27 2021

@author: mahan
"""

def display(solution_number, board):
    row = '|   ' * len(board) + '|'
    hr  = '+---' * len(board) + '+'
    for col in board:
        print(hr)
        print(row[:col*4-3],'Q',row[col*4:])
    print(f'{hr}\n{board}\nSolution - {solution_number}\n')


def is_safe(q, board, x=1):
    if not board: return True
    if board[-1] in [q+x,q-x]: return False
    return is_safe(q, board[:-1], x+1)

def solve(boardsize, board = [], num = 0):
    if board and len(board)==boardsize:
        num += 1
        display(num, board)
    else:
        for q in [col for col in range(1, boardsize+1) if col not in board]:
            if is_safe(q, board):
                num = solve(boardsize, board+[q], num)
    return num

def solveNQueens(n, board = []):        
    if board and len(board) == n:
        str_list = []
        for r in board:
            row = "."*(r-1) + "Q" + "."*(n-r)
            str_list.append([row])
        print(str_list)
    
    for i in [c for c in range(1, n+1) if c not in board]:
        if is_safe(i, board):                
            solveNQueens(n, board + [i])
        

solveNQueens(4)