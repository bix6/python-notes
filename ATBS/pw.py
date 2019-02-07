#!/usr/bin/env python3
#pw.py - An insecure password locker program.

PASSWORDS = {'email': ' FJoiwoi9829344u19889',
             'blog': 'joiasWiojso*$#(lsikj',
             'luggage':'12345'}

import sys, pyperclip
if len(sys.argv) < 2: #makes sure user calls program with an account name
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # 0 is script name, 1 is 1st argument = account

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
