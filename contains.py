#!/usr/bin/env python3.9

import argparse

parser = argparse.ArgumentParser(description='Search for words including partial word')
parser.add_argument('snippet', help='partial (or complete) string to search for in words')

args = parser.parse_args()
snippet = args.snippet.lower()

with open('/usr/share/dict/words') as f:
    words = f.readlines()

matches = []

#for i in words:
#    if snippet in i.lower():
#        matches.append(i)

# We're using list comprehension instead
matches = [ word for word in words if snippet in word.lower()]
# [ word is the first parameter above, and indicates what will be added to the list ]
# https://docs.python.org/3/tutorial/datastructures.html
# https://www.w3schools.com/python/python_lists_comprehension.asp



print(matches)
