# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 23:04:12 2020

@author: Prasa
"""


def calculator(num1, num2):
    total = num1+num2
    return total

print( calculator(6,10))

def cc1(no1, no2):
    to = no1+no2
    print("{} + {} = {}".format(no1, no2, to))

a = 10
type (a)

def Calc1(n1, n2, method = "add"):
    if method == "add":
        print(n1 + n2)
    if method == "sub":
        print(n1 - n2)
Calc1(10,2,"sub")