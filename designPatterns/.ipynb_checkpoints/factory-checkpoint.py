#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  3 15:37:39 2021

@author: mahan
"""

class Person(object):
    fName, lName = "", ""
    
    def __init__(self, fName, lName):
        self.fName = fName
        self.lName = lName
    
    def getName(self):
        return f'{self.fName} {self.lName}'
    
class Male(Person):    
    def getName(self):
        return "Mr. " + Person.getName(self)
       
class Female(Person):
    def getName(self):
        return "Ms. " + Person.getName(self)

class PersonFactory():
    def createPersons(self, typ, fName, lName):
        typ = typ.capitalize()
        return globals()[typ](fName, lName)
    
if __name__ == "__main__":
    pFactory = PersonFactory()
    for t in ['Male', 'Female']:
        obj = pFactory.createPersons(t, "mik", "de")
        print (obj.getName())