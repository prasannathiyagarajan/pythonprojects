# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 23:11:17 2020

@author: Prasa
"""
lst = []
###lstnumbers = input ("Enter the numbers")
'''a = input ("Enter 1st number : ")
lst.append(a)
print (f"Given number : {a} is added to the list LST")
print (lst)
###print (f"Given number is : {lstnumbers}")
'''
a = input ("Enter no of entries to be loaded in list: ")
for i in range(int(a)):
    i = int(input("Enter number to add in list"))
    lst.append(i)
print (f"Given number : {lst} is added to the list LST")
print (lst)
lst.sort()
### index - reverse
print(f"Smallest number in the list = {lst[0]}")
print(f"Biggest number in the list = {lst[-1]}")
print(lst)

for j in lst:
    if j % 2 == 0:
        ###print (f"Even numbers are = {j}")
        print (j, end = "")

ev_no =[n for n in lst if n%2==0]
print (ev_no)