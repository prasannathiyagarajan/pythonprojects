# -*- coding: utf-8 -*-

# importing required modules 
import PyPDF2 
import argparse as ap



def readPDFfile(fpath):
    # creating a pdf file object 
    #pdfFileObj = open('C:/Users/Prasa/Documents/Tutorial/conda-cheatsheet.pdf', 'rb') 
    #print(fpath)
    pdfFileObj = open(fpath, 'rb') 

    # creating a pdf reader object 
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # printing number of pages in pdf file 
    print(pdfReader.numPages)

    # creating a page object 
    pageObj = pdfReader.getPage(0)

    # extracting text from page 
    print(pageObj.extractText())

    # closing the pdf file object 
    pdfFileObj.close()  
    

if __name__ == '__main__':
    parser = ap.ArgumentParser()
    #parser.add_argument('file', help="Enter valid file path")
    parser.add_argument("filepth", help="Enter filepath")
    args = parser.parse_args()
    #print(args)
    readPDFfile(args.filepth)
    