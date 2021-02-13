#!/usr/bin/env python3.9

from argparse import ArgumentParser

parser = ArgumentParser(description='Read a file line and handle errors')
parser.add_argument('file_name', type=str, help='file name')
parser.add_argument('line_number', type=int, help='number of the line to be read')

args = parser.parse_args()


file_name = args.file_name
line_number = args.line_number

print(f"File name: {file_name}; Line number: {line_number}.")

try:
    with open(file_name, "r") as f:
        lines = f.readlines()
        #print(len(lines))
        line = lines[line_number-1]
        print(line)
# Error types in python
# https://www.tutorialsteacher.com/python/error-types-in-python
except IndexError:
    if line_number > len(lines):
        print("Number of the line provided is higher that the number of lines on the file")
