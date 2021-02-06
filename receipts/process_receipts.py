import os
import glob
import json
import shutil

try:
    ## https://docs.python.org/3/library/os.html#os.mkdir
    os.mkdir('./processed')
except OSError:
    print("'processed' directory already exists.")

## https://docs.python.org/3/library/glob.html
receipts = glob.glob('./new/receipt-[0-9]*.json')
subtotal = 0.0

for path in receipts:
    with open(path) as f:
        ## https://docs.python.org/3/library/json.html
        content = json.load(f)
        subtotal += float(content["value"])
    name = path.split("/")[-1]
    destination = f"./processed/{name}"
    ## https://docs.python.org/3/library/shutil.html
    shutil.move(path, destination)
    print(f"moved '{path}' to '{destination}'")

print("Receipt subtotal: $%.2f" % subtotal)
print(f"TESTE: Receipt subtotal: ${subtotal}")
