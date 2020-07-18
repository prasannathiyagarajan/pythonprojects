# -*- coding: utf-8 -*-

import argparse
#parser = argparse.ArgumentParser()
#parser.parse_args()
parser = argparse.ArgumentParser()
parser.add_argument('book', default="JournalDev", help="enter a text",type=int)
parser.add_argument('author', default="Anup", help="enter author name")
args = parser.parse_args()
print(args)
if args.book == 'JournalDev':
    print('You made it!')
else:
    print("Didn't make it!")