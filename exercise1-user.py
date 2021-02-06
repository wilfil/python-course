#!/usr/bin/env python3.9

#import argparse

#parser = argparse.ArgumentParser(description='Search for words including partial word')
#parser.add_argument('snippet', help='partial (or complete) string to search for in words')

#args = parser.parse_args()
#snippet = args.snippet.lower()
#users = []
"""
user1 = { 'admin': True,  'active': False, 'name': 'Kevin'  }
user2 = { 'admin': False, 'active': True,  'name': 'Wilson' }
user3 = { 'admin': True,  'active': True,  'name': 'Sandra' }

users=[user1,user2,user3]
print(users)



for user in users:
    if user["admin"] and user["active"]:
        print(f'ACTIVE - (ADMIN) {user["name"]}')
    elif user["admin"]:
        print(f'(ADMIN) {user["name"]}')
    elif user["active"]:
        print(f'(ACTIVE) - {user["name"]}')
"""
users = [
            { 'admin': True, 'active': True, 'name': 'Kevin' },
            { 'admin': True, 'active': False, 'name': 'Elisabeth' },
            { 'admin': False, 'active': True, 'name': 'Josh' },
            { 'admin': False, 'active': False, 'name': 'Kim' },
        ]

line = 1

for user in users:
    prefix = f"{line} "

    if user['admin'] and user['active']:
        prefix += "ACTIVE - (ADMIN) "
    elif user['admin']:
        prefix += "(ADMIN) "
    elif user['active']:
        prefix += "ACTIVE - "

    print(prefix + user['name'])
    line += 1
