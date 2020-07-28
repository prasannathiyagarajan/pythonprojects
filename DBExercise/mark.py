# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 08:24:18 2020

@author: Mathu
"""
import db_connection as dbc

def insert_record(cn,query):
    #query=f"INSERT INTO test (name,mark) VALUES ('{name}','{mark}')"
    cn.execute_query(query)
    print("Inserted successfully")
    
    
def fetch_record(cn,query):
    #query_fetch="select * from test"
    rows=cn.fetch_data(query)
    return rows
    

  
if __name__ =="__main__":
    cn = dbc.sqllite_db_connector()    
    #get data
    name = input("Enter the name")
    mark = input("Enter the mark")
    #inser data
    query=f"INSERT INTO test (name,mark) VALUES ('{name}','{mark}')"
    insert_record(cn,query)
    
    q= "select * from test"
    row=fetch_record(cn,q)
    for r in row:
        print(r)
    #fetch data
    
