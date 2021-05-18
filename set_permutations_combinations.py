#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 14:44:50 2021

@author: mahan
"""

def factorial(number):
    def is_negative(number):     
        if number < 0:
            raise Exception("negative")
    try:
        is_negative(number)
    except:
        print("number must be a positive integer")
    else:
        return 1 if number <= 1 else number * factorial(number - 1)

def get_all_pemutations(list_char = ['1','2','a','b']):
    permutations = []
    for i in range(factorial(len(list_char))):
        l_char = list_char.copy()
        permutation = []
        while l_char:
            count = factorial(len(l_char)-1)
            select = i//count
            permutation.append(l_char[select])
            del(l_char[select])
            i -= count * select
        permutations.append(permutation)
    return permutations

def all_perms(elements= ['1','2','a','b']):
    if len(elements) <=1:
        yield elements
    else:
        for i in range(len(elements)):
            for perm in all_perms(elements[1:]):
                yield perm[:i] + elements[0:1] + perm[i:]
                
def getElementFromEachList(l=[['1', '2'],['a', 'b']]):
    if len(l) == 1:
        return [[x] for x in l[0]]
    result = []
    for listElements in getElementFromEachList(l[1:]):
        for fElement in l[0]:
            result.append([fElement] + listElements)
    return result

def getPermutations(l=['a','b','c'], r=2):
    results = []
    def getPermutationsRecr(l, com = []):
        if len(com) == r:
            results.append(com)
            return
        for e in l:
            li = list(l)
            li.remove(e)
            getPermutationsRecr(li, com + [e])
    
    getPermutationsRecr(l)
    return results

def getCombinations(l=['a','b','c'], r=2):
    results = []
    def getCombinationsRecr(l, com = []):
        if len(com) == r:
            results.append(com)
            return

        for i, e in enumerate(l):
            getCombinationsRecr(l[i+1:], com + [e])
    
    getCombinationsRecr(l)
    return results

print(getCombinations())

