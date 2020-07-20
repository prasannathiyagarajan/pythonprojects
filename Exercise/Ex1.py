# -*- coding: utf-8 -*-

#Input fil using cmd prompt and printing

#import necessary packages

import argparse as ap
import os
import csv

#Create ArgParser

#Check input File extension
def checktypeofFile(file):
    '''
    Parameters
    ----------
    file : TYPE
        Enter File Path.

    Returns
    -------
    TYPE
        Returns the File Extn of the given file.

    '''
    ext = file.split(".")
    print(ext[1])
    return ext[1]

#write a function to read a file (CSV)

def readcsvfile(file):
    '''
    

    Parameters
    ----------
    file : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    fields = []
    rows = []
    with open(file, 'r') as csvfile:
        # creating a csv reader object 
        csvreader = csv.reader(csvfile) 
    
        # extracting field names through first row 
        fields = next(csvreader) 
  
        # extracting each data row one by one 
        for row in csvreader:
            print(row)
            rows.append(row) 
  
        # get total number of rows 
        print("Total no. of rows: %d"%(csvreader.line_num)) 
  
        # printing the field names 
        print('Field names are:' + ', '.join(field for field in fields)) 
  
        #  printing first 5 rows 
        print('\nFirst 5 rows are:\n') 
        for row in rows[:5]: 
            # parsing each column of a row 
            for col in row: 
                print("%10s"%col), 
                print('\n') 

def readdocfile(file):
    with open(file, 'r') as docfile:
        
        for line in docfile:
            print(line)

def writefile(file):
    with open(file, 'a', encoding='ascii') as f:
        strText = input("Enter the text to append :- ")
        f.write("\n")
        f.write(strText)
        print("File has been updated with the contents provided", args.file)
        
#Write a function to read and print CSV file



#main method

if __name__ == '__main__':
    parser = ap.ArgumentParser()
    parser.add_argument('file', help="Enter File Path")
    parser.add_argument('-method', default="read", dest="method", help="Enter Read or Write")
    args = parser.parse_args()
    print(args)
    ext = checktypeofFile(args.file)
    
    if args.method == "read":
        if ext == "csv":
            readcsvfile(args.file)
        elif ext == "docx":
            readdocfile(args.file)
        else:
            print ("Given File is not valid")
    elif args.method == "write":
        writefile(args.file)
        '''if ext == "csv":
            print("Write CSV")
        elif ext == "docx":
            print("Write DOC")
            writefile(args.file)
        else:
            print("Give a valid doc")
'''



