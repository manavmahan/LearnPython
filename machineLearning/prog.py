#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 26 13:12:31 2021

@author: mahan
"""

class Obj():
    a = None; b = None
    def __init__(self):
        self.a = 1
        self.b = 1
    
    def __repr__(self):
       return f"{self.a}, {self.b}"
        
    def __str__(self):
        return f"{self.a}, {self.b}"