# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 23:11:17 2020

@author: Prasa
"""

number = int (input("Enter Number "))
a = 1
b = 10
for i in range(a, b+1):
    value = number * i
    print (f"{number} * {i} = {value}")
    