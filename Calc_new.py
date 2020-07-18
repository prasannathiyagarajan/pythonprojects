# -*- coding: utf-8 -*-

def calculate(x,y,method):
    if method == "add":
        return x+y
    if method == "sub":
        return x-y
    
if __name__ == "__main__":
    a = int(input("Enter 1st number "))
    b = int(input("Enter 2nd number "))
    c = input("Enter Method ")
    d = calculate(a,b,c.lower())
    print (d)