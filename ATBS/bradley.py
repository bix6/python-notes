import re
bradRegex = re.compile(r'Brad (really|always)? like(s)? dicks')
mo1 = bradRegex.search('''It was a sunny day and Brad was munching on some dicks
Brad really likes dicks, it seems. We wonder, will Brad always like dicks?
The future is uncertain but one thing is for sure: Brad likes dicks.''')
print(mo1.group())
