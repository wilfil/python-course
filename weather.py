#!/usr/bin/env python3.9
# ###!/home/aves/bin/venvs/experiment/bin/python3.9

# pip install requests
# https://pypi.org/project/requests/
# To activate venv: source venvs/experiment/bin/activate

import sys
import requests
import os

from argparse import ArgumentParser

parser = ArgumentParser(description='Get the weather information from OpenWeatherMap API.')
parser.add_argument('zip', default='20020', help='ZIP/Postal Code')
parser.add_argument('--country', '-c',  default='us', help='Country Code. Ex: US, CA, BR, etc. Default is US.')


args = parser.parse_args()
#print(args)

api_key= os.getenv('API_KEY')

if not api_key:
    print("Error: no 'API_KEY' set")
    sys.exit(1)

response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?zip={args.zip},{args.country}&appid={api_key}")

if response.status_code != 200:
    print(f"Error talking to weather provider: {response.status_code}")
    sys.exit(1)


print(response.json())
