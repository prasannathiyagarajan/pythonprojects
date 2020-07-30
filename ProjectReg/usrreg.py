# -*- coding: utf-8 -*-
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from usrdb import staffuser
engine = create_engine('sqlite:///schoolprj.db', echo = True)
meta = MetaData()

'''
staffuser = Table(
   'staffuser', meta, 
   Column('id', Integer, primary_key = True), 
   Column('firstname', String), 
   Column('lastname', String),
   Column('usrid', String),
   Column('password', String)
)
'''

fn = input("Enter First Name - ")
ln = input("Enter Last Name - ")
usrid = input("Enter User ID - ")
usrpwd = input("Enter Password - ")


ins = staffuser.insert().values(firstname = fn, lastname = ln, usrid = usrid, password = usrpwd)
result = engine.execute(ins)