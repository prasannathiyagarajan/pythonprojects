# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 07:54:42 2020

@author: Mathu
"""

from flask import Flask, render_template
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('sqlite:///webprj.db')

app = Flask(__name__)

@app.route('/hello/<user>')
def hello_name(user):
    print("I m in side hello_name func")
    return render_template('hello.html', name = user, age=21)

@app.route('/people/<fname>/<lname>/<usrid>/<pwd>')
def people(fname,lname,usrid, pwd):
    print("Inside the people function")
    query = f"INSERT INTO staffuser (firstname,lastname,usrid, password) VALUES('{fname}', '{lname}', '{usrid}', '{pwd}')"
    print(query)
    engine.execute(query)
    print("values are stored in table")
    return render_template("usrreg.html", fname=fname, lname=lname, usrid = usrid, pwd = pwd)

def createDBtbl():
    
    meta = MetaData()

    staffuser = Table(
    'staffuser', meta, 
    Column('id', Integer, primary_key = True), 
    Column('firstname', String), 
    Column('lastname', String),
    Column('usrid', String),
    Column('password', String)
    )
    
    studentmstr = Table(
    'studentmstr', meta,
    Column('firstname', String), 
    Column('lastname', String),
    Column('deptname', String),
    )
    meta.create_all(engine)

if __name__ == '__main__':
    print("in Main")
    
    createDBtbl()

    app.run()
