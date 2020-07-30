# -*- coding: utf-8 -*-

import pandas as pd
from config import engine, meta, Table, Column, Integer, String

class tblcreation():
    def __init__(self):
        self.staffuser = Table(
            'staffuser', meta, 
            Column('id', Integer, primary_key = True), 
            Column('firstname', String), 
            Column('lastname', String),
            Column('usrid', String),
            Column('password', String)
            )
        
        self.studentmstr = Table(
            'studentmstr', meta,
            Column('firstname', String), 
            Column('lastname', String),
            Column('deptname', String),
            )
    
        meta.create_all(engine)