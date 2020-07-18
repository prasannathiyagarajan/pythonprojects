# -*- coding: utf-8 -*-

import datetime

def convertdatetime(date):
    dtDate = date.split("/")
    retDate = datetime.datetime(int(dtDate[2]), int(dtDate[1]), int(dtDate[0]))
    return retDate

def convertyyyymmdd(date):
    dtDateTime = date.split(" ")
    print(dtDateTime)
    dtDate = dtDateTime[0].split("/")
    print(dtDate)
    retDate = (dtDate[2] + "/" + dtDate[1] + "/" + dtDate[0])
    return retDate

def formatchange(date):
    dt_1 = date.split("/")
    return dt_1[2]+dt_1[1]+dt_1[0]
    
if __name__ == "__main__":
    dt = input("Enter Date as DD/MM/YYYY - ")
    dDateTime = convertdatetime(dt)
    print(f"Given date {dt} is converted to date time as {dDateTime}")
        
    dYYYYMMDD = convertyyyymmdd(dt)
    print(f"Given date {dt} is converted to YYYY/MM/DD as {dYYYYMMDD}")
    
    dt2 = formatchange(dt)
    print (dt2)
    
    
    
    