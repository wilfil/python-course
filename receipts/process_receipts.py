import os
import glob
import json
import shutil
import math

try:
    ## https://docs.python.org/3/library/os.html#os.mkdir
    os.mkdir('./processed')
except OSError:
    print("'processed' directory already exists.")

## https://docs.python.org/3/library/glob.html
receipts = glob.glob('./new/receipt-[0-9]*.json')
subtotal = 0.0

## or.. for path in glob.iglob('./new/receipt-[0-9]*.json')
for path in receipts:
    with open(path) as f:
        ## https://docs.python.org/3/library/json.html
        #print(f)
        content = json.load(f)
        #print(content)
        subtotal += float(content["value"])
    #name = path.split("/")[-1]
    #destination = f"./processed/{name}"
    destination = path.replace('new', 'processed')
    ## https://docs.python.org/3/library/shutil.html
    shutil.move(path, destination)
    print(f"moved '{path}' to '{destination}'")

print("Receipt subtotal: $%.2f" % subtotal)
print(f"TESTE: Receipt subtotal: ${round(subtotal,2)}")
#print(f"TESTE: Receipt subtotal: ${math.ceil(subtotal)}")
#print(f"TESTE: Receipt subtotal: ${math.floor(subtotal)}")
