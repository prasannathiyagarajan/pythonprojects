# -*- coding: utf-8 -*-

import sys

def calculate(x,y,method):
    if method == "add":
        return x+y
    if method == "sub":
        return x-y
    
if __name__ == "__main__":
    print(sys.argv)
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = sys.argv[3]
    '''a = int(input("Enter 1st number "))
    b = int(input("Enter 2nd number "))
    c = input("Enter Method ")
    '''
    d = calculate(a,b,c.lower())
    print (d)