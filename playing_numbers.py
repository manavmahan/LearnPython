#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 23:52:08 2021

@author: mahan
"""
def factorial(number):
    return 1 if number <= 1 else number * factorial(number - 1)

def is_even(number):
	return not bool(number % 2)

def is_prime(number):
    for i in range(2, number//2):
        if number % i == 0:
            return False
    return True

def is_strong_number(number):
    return sum([factorial(int(x)) for x in str(number)]) == number

def is_armstrong_number(number):
    digit_list = list(str(number))
    n_digits = len(digit_list)
    sum_value = sum([int(x) ** n_digits for x in digit_list])
    return sum_value == number
	
def get_divisors (number):
	return [i for i in range(1, number//2 + 1) if number % i == 0]
	
def is_perfect_number (number):
	return sum(get_divisors (number)) == number

def is_super_perfect_number (number):
    first_sum = sum(get_divisors(number)) + number
    return sum(get_divisors(first_sum)) + first_sum == 2 * number

def get_digits(x, digits = []):
    return get_digits(x//10, digits + [x%10]) if x>0 else digits

def get_number(li, pos = 0, num = 0):
    return get_number(li[1:], pos + 1, num + li[0] * 10 ** pos) if li else num