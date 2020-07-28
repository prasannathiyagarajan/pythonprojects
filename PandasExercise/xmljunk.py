# -*- coding: utf-8 -*-

import csv
import requests
import xml.etree.ElementTree as ET

def parseXML(xmlfile):
    #print(xmlfile)
    #with open(xmlfile, 'r') as f:
     #   f.read()
    
    # create element tree object
    tree = ET.parse(xmlfile)
    
    # get root element
    root = tree.getroot()
    
    # create empty list
    custfeed = []
    
    # iterate news items 
    for item in root.findall('./Transaction/CustTrans'):
        # empty dictionary
        custdata = {}
        
        # iterate child elements of item 
        for child in item:
            custdata[child.tag] = child.text
            print(child.text)
        

def parseXMLfeed(xmlfile):
      
    # create element tree object 
    tree = ET.parse(xmlfile)
      
    # get root element 
    root = tree.getroot()
      
    # create empty list for news items 
    newsitems = [] 
  
    # iterate news items 
    for item in root.findall('./Transaction/CustTrans'): 
  
        # empty news dictionary 
        news = {}
          
        # iterate child elements of item 
        for child in item: 
  
            # special checking for namespace object content:media 
            if child.tag == '{http://search.yahoo.com/mrss/}content': 
                news['media'] = child.attrib['url'] 
            else:
                print(child.text)
                news[child.tag] = child.text
                #news[child.tag] = child.text.encode('utf8') 
  
        # append news dictionary to news items list 
        newsitems.append(news) 
      
    # return news items list 
    
    return newsitems 
        
def main():
    #lstCustFeed = parseXML("C:/Users/Prasa/PythonSamples/PandasExercise/Samplexml.xml")
    lstCustFeed123 = parseXMLfeed("C:/Users/Prasa/PythonSamples/PandasExercise/Samplexml.xml")
    

if __name__ == "__main__":
    main()