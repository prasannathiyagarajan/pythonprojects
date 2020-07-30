# -*- coding: utf-8 -*-

from config import engine
from tblnames import tblcreation

tc = tblcreation()

fn = input("Enter First Name - ")
ln = input("Enter Last Name - ")
usrid = input("Enter User ID - ")
usrpwd = input("Enter Password - ")

ins = tc.staffuser.insert().values(firstname = fn, lastname = ln, usrid = usrid, password = usrpwd)
result = engine.execute(ins)
