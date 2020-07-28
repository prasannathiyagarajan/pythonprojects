# -*- coding: utf-8 -*-
'''
DB connector
'''

#package import for the DB
import sqlite3
#import config as c
from sqlite3 import Error

class sqllite_db_connector():
    
    def __init__(self):
        '''
        connection striing define
        '''
        self.db_file = "test.db"
    
    def connect(self):
        '''
        Establish Connection
        '''
        try:
            self.con = sqlite3.connect(self.db_file)
        except Error as e:
            print(e)
        return self.con
    
    def execute_query(self,query):
        '''
        Input: Query
        Process: execute and returns the result
        '''
        con = self.connect()
        with con:
            cur = con.cursor()
            res=cur.execute(query)
        
        cur.close()
        return res
            
    def fetch_data(self,query):
        con = self.connect()
        with con:
            cur = con.cursor()
            cur.execute(query)
            rows = cur.fetchall()
        return rows
    
    def close(self):
        """
        Closes the cursor and connection of the database.
        """        
        self.conn.close()

