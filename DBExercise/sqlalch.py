# -*- coding: utf-8 -*-

import pandas as pd

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('sqlite:///college.db', echo = True)
meta = MetaData()

students = Table(
   'students', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String), 
   Column('lastname', String)
)
'''
meta.create_all(engine)

fnm = input("Enter user name - ")
lnm = input("Enter Last name - ")

ins = students.insert().values(name = fnm, lastname = lnm)
result = engine.execute(ins)
'''
print(engine.execute("SELECT * FROM students").fetchall())
'''s = students.select()
result1 = engine.execute(s)
print(result1.fetchall())
'''
#-------------------------------------------------------------
'''
import pandas as pd

from sqlalchemy import create_engine
engine = create_engine('sqlite:///data.db', echo=False)



df = pd.read_csv("data.csv")
df.to_sql('data_table',con=engine, )

engine.execute("SELECT * FROM data").fetchall()
'''