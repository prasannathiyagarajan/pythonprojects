# -*- coding: utf-8 -*-
import pandas as pd

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

engine = create_engine('sqlite:///schoolprj.db')

meta = MetaData()

staffuser = Table(
   'staffuser', meta, 
   Column('id', Integer, primary_key = True), 
   Column('firstname', String), 
   Column('lastname', String),
   Column('usrid', String),
   Column('password', String)
)

meta.create_all(engine)
