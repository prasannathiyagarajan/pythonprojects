# -*- coding: utf-8 -*-

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-method', default="add", dest="method", help="Enter a valid method")
parser.add_argument('n1', help="Enter a number", type = int)
parser.add_argument('n2', help="Enter a number", type = int)

args = parser.parse_args()

print(args)

if args.method == "add":
    print(args.n1+args.n2)
elif args.method == "sub":
    print(args.n1-args.n2)
    
    






