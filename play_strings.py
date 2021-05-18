#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 22:26:56 2021

@author: mahan
"""

import re

def is_palindrome(string):
    return string == string[::-1]

def is_number_palindrome(number):
    return str(number) == str(number)[::-1]

def find_vowels_count(string):
    vowels = dict()
    for vowel in re.findall('[a,e,i,o,u]', string):
        vowels[vowel] = string.count(vowel)
    return {x:vowels[x] for x in sorted(vowels)}

def get_zig_zag_string(s, n = 3):
    '''
    type s: str
    type n: int
    rtype: str
    
    s = PAYPALISHIRING
    n = 3 string = PAHNAPLSIIGYIR
    n = 4 string = PINALSIGYAHRPI
    '''
    
    string = ''
    for r in range(n):
        for i, c in enumerate(s):
            if i % (2 * (n - 1)) == r or (i + r) % (2 * (n - 1)) == 0:
                string += c
                
    str_list = ['' for x in range(n)]
    row = 0
    step = 1
    for i, c in enumerate(s):
        str_list[row] += c
        if row==0:
            step = 1
        if row == n - 1:
            step = -1
        row += step
    
    return string == ''.join(str_list)

#https://leetcode.com/problems/regular-expression-matching/
def get_matching_pattern_star_dot(string, pattern):
    if not pattern: return not string    
    first_match = bool(string) and pattern[0] in {string[0], '.'}
    
    if (len(pattern) >= 2 and pattern[1] == '*'):
        return get_matching_pattern_star_dot(string, pattern[2:]) or first_match and get_matching_pattern_star_dot(string[1:], pattern)
    
    return first_match and get_matching_pattern_star_dot(string[1:], pattern[1:])
            
print(get_zig_zag_string('PAYPALISHIRING', 3))