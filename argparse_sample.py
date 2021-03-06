#!/usr/bin/env python3.9

# Hint: Use "yyp" to duplicate a line in VIM

import argparse
import sys

parser = argparse.ArgumentParser(description='Read a file in reverse');
parser.add_argument('filename', help='The file to read');
parser.add_argument('--limit', '-l', type=int, help='The number of lines to read');
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0');

# args receive the command with the arguments
args = parser.parse_args();

try:
    f = open(args.filename)
    limit = args.limit
except FileNotFoundError as erro:
    print(f"I've got this error: {erro}")
    sys.exit(2)

#except:
#    print(f"Testing")

else:
    with open(args.filename) as f:
        lines = f.readlines()
        print(lines)
        lines.reverse()
        print(lines)

        if args.limit:
            lines = lines[:args.limit]

        for line in lines:
            print(line.strip()[::-1]) ##That's how we reverse a string in python
            #print(line.strip())


#finally:
#    print("Finally")
