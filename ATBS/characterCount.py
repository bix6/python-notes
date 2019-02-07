import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
pprint.pprint(count) # pretty pring dict vals
myStr = pprint.pformat(count) # pformat gives you the vals as a string
