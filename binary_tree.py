#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 11:08:02 2021

@author: mahan
"""

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
    def __repr__(self):
        return self.__str__()
        
    def __str__(node):
        s = ""
        if node:
            s += "TreeNode{val: " + str(node.val) 
        if node.left:
            s += ", left: {" + node.left.__str__() + '}'
        if node.right:
            s += ", right: {" + node.right.__str__() + '}'
         
        if node:
            s += '}'
        
        return s
        
def printTree(node):
    if not node: 
        return      
    print(node.val)
    printTree(node.left) 
    printTree(node.right)
    
def arrayToTree(array):
    if array:
        node = Node(array[0])
        
        l, r = [[1, 2]], [[2, 3]]
        n, co = 1, 3
        while co < len(array):
            l_start = r[-1][-1]
            l.append([l_start, l_start + 2 * n])
                        
            r_start = l[-1][-1]
            r.append([r_start, r_start + 2 * n])
            n *= 2
            co += 4 * n 
        
        left_array, right_array = [], []
        
        for l_index, r_index in zip(l, r):
            left_array += array[l_index[0]: l_index[1]]
            right_array += array[r_index[0]: r_index[1]]
        
        node.left = arrayToTree(left_array)
        node.right = arrayToTree(right_array)
        return node
        
tree = None
# nodes = list(map(int, input().split()))
# print(nodes)

root = [4,2,3,1,7,6,9]

def invert_tree(root = None):
    if root:
        root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root

def is_bst(root = None):
    if root.left and root.right:
        if root.left.val > root.right.val:
            return False
        else:
            return is_bst(root.left) and is_bst(root.right)
    return True

root = arrayToTree(root)
print(root)


print(is_bst(root))