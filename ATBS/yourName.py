name = ''
while name != 'Jack':
    print('Please type your name:')
    name = input()
print('Thank you!')

while True:
    print('Please type your name:')
    name = input()
    if name == 'JackJack':
        break
print('Thank you!')

while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('What is the password, Joe?')
    password = input()
    if password == 'swordfish': # This needs another loop cuz it restarts loop if password is wrong
        break
print('Access granted.')

name = ''
while not name:
    print('Enter your name:')
    name = input()
print('How many guests will you have?')
numOfGuests = int(input())
if numOfGuests:
    print('Be sure to have enough room for all your guests.')
print('Done')
