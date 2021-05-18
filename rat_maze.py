#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 19:22:24 2021

@author: mahan
"""

maze = [[1, 0, 0, 0],
        [1, 1, 0, 1], 
        [0, 1, 0, 0], 
        [1, 1, 1, 1],
        [0, 1, 1, 1]]

def is_safe(maze, sol, x, y):
    return x>=0 and y>=0 and x<len(maze) and y<len(maze[0]) and maze[x][y] == 1 and sol[x][y] == 0

def solve_maze(maze, x, y, sol):
    # solution found
    if x == len(maze) -1 and y == len(maze[0]) - 1:
        sol[x][y] = 1
        return True
    
    moves = [[0,1],[0,-1],[1,0],[-1,0]]
    
    #possible solution
    for m in moves:
                
        # is possible move/ constraint
        if is_safe(maze, sol, x, y):
            sol[x][y] = 1
        
            #recursion condition if part of solution
            if solve_maze(maze, x + m[0], y + m[1], sol):
                return True
        
            #backtrack
            sol[x][y] = 0
    return False
    
def solveMaze( maze ):
    sol = [ [ 0 for j in range(len(maze[0])) ] for i in range(len(maze)) ]
     
    if solve_maze(maze, 0, 0, sol) == False:
        print("Solution doesn't exist");
        return False
     
    print(sol)
    return True

solveMaze(maze)