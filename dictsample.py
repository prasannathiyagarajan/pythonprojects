# -*- coding: utf-8 -*-

emp = []
emp_info = {"user": {"name" : "Prasanna", "age" : "35", "department": "IT"}}
emp.append(emp_info)

emp_info1 = {"user": {"name" : "Maddy", "age" : "36", "department": "HR"}}
emp.append(emp_info1)

org_info = {"OrgName" : {"name", "CTS"}}
emp.append(org_info)
org_info1 = {"OrgName" : {"name", "Infosys"}}
emp.append(org_info1)

emp_info["OrgName"] = "Infosys"
emp_info1["user"]["OrgName"] = "Infosys"

print(emp_info)
print(emp_info1)
print (len(emp))
print(emp)
print(emp[1]["user"]["name"])