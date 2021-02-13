from argparse import ArgumentParser
import shlex, subprocess
import os,sys,requests,json

parser = ArgumentParser(description="Gets the content of a webpage and writes to a file")
parser.add_argument("url", type=str, help="URL to be copied")
parser.add_argument("dest_file", type=str, help="Destination file")
parser.add_argument("--content_type", "-c", type=str, default="text", help="Optional content type must be text or json. Default is text")

args = parser.parse_args()

r = requests.get(args.url)

# Check if the URL exists
if r.status_code >= 400:
    print(f"Pagina {args.url} nao encontrada")
    sys.exit(1)

else:
    ## Convert the content to json
    if args.content_type == "json":
        try:
            content = r.json()
            with open(args.dest_file, 'w', encoding='UTF-8') as f:
                json.dump(content, f)
        except ValueError:
            print("web content cannot be converted to a json file.")
            sys.exit(1)
    # Default for txt files
    else:
        content = r.text
        with open(args.dest_file, 'w', encoding='UTF-8') as f:
    #for chunk in r.iter_content(chunk_size=128):
            f.write(content)

"""
headers['content-type']
'application/json; charset=utf8'
r.encoding
'utf-8'
 r.text
'{"type":"User"...'
 r.json()
{'disk_usage': 368627, 'private_gists': 484, ...}
"""
