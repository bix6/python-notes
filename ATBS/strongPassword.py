#! python3
# strongPassword.py - detects a strong password (8+ chars, upper and lower case, 1+ digits)

import re

def passChecker(passIn):
    if len(passIn) < 8:
        return False
    
    charRegex = re.compile(r'([a-z])+')
    if charRegex.search(passIn) == None:
        return False

    charRegex2 = re.compile(r'([A-Z])+')
    if charRegex2.search(passIn) == None:
        return False
    
    numRegex = re.compile(r'\d+')
    if numRegex.search(passIn) == None:
        return False
    return True

print(passChecker('Hey'))
print(passChecker('abcdefghijklmnop'))
print(passChecker('abcdefghijklmnop12345'))
print(passChecker('abcdefghijklmnop12345ABC'))
print(passChecker('12345ABC'))
print(passChecker('a12AB'))
