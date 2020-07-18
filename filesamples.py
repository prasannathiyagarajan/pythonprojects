# -*- coding: utf-8 -*-
'''with open('new_file.txt', 'w', encoding='ascii') as f:
    f.write("This is a sample line of text\n")
    f.write("Yet another line\n")
'''
'''
filename = 'new_file.txt'
f = open(filename, 'r', encoding='ascii')
#for line in f:
#   print (line)
a = f.readlines()
print(a)
f.close()
#print("Contents of " + f.read())
'''

###W - write
###a - appened

a = """
My name is prasanna
my boss is maddy
training in python
"""
b = input("Enter a string to append : ")
with open('user_inpfile.txt', 'a', encoding='ascii') as f:
    f.write(a)
    f.write(b)
    