# -*- coding: utf-8 -*-

import db_connection as dbc

pras = dbc.sqllite_db_connector()

query = '''
    CREATE TABLE test(
  name text null,
  mark text null
)
'''
#pras.execute_query(query)

query_ins = "INSERT INTO test (name,mark) VALUES ('maddy','99')"
pras.execute_query(query_ins)
#print("Query executed")

query_sel = "SELECT * FROM test"
rows = pras.fetch_data(query_sel)

for row in rows:
    print(row)

