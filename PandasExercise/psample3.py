# -*- coding: utf-8 -*-
import requests
import pandas as pd
import csv

# =============================================================================
# url = "https://jsonplaceholder.typicode.com/todos"
# data1 = requests.get(url).json()
# print(len(data1))
# #print(data1)
# print(data1[:5])
# print(type(data1))
# df2 = pd.DataFrame(data1)
# print(df2)

#df2.to_csv('users.csv')
# =============================================================================



url2 = "https://jsonplaceholder.typicode.com/todos/2"
data2 = requests.get(url2).json()
print(data2)
dframe = pd.DataFrame([data2])

url3 = "https://jsonplaceholder.typicode.com/todos/2"
data3 = requests.get(url3).json()
print(data3)
dframe = pd.DataFrame([data3])

dlist = []
for i in range(1,10):
    url=f"https://jsonplaceholder.typicode.com/todos/{i}"
    #print(f"value of i is {i} and the URL is {url}")
    data = requests.get(url).json()
    dlist.append(data)
#print(type(dlist))
#print(dlist)

df = pd.DataFrame(dlist)
print(df)


#df = pd.DataFrame(data])
#print(df.head())