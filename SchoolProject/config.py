# -*- coding: utf-8 -*-

import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

engine = create_engine('sqlite:///schoolproject.db')

meta = MetaData()

meta.create_all(engine)