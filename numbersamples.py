# -*- coding: utf-8 -*-


num1 = 7
num2 = 10
'''add - sub

'''
total = num1 + num2

'''Float Output using single slash
total = num1 / num2
'''

'''Float Output gives only integer portion when using double slash
total = num1 // num2
'''

print("Sum of numbers", num1, "+", num2, " = ", total)


def calculator(n1, n2, method = "add"):
    if method == "add":
        print (method, "of ",n1, "and ", n2, "is",  n1 + n2)
    if method == "sub":
        print (n1 - n2)
calculator(10,2,"add")

a = 8
type(a)
    
    
