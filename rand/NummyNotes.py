# NummyNotes.py

# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == "__main__":
# When python reads source file, it executes all code found in it.
# Befor execution will define some vars including __name__ to "__main__"
# if file is imported from another module then __name__ will be modules name
# So if we run the file directly (e.g. python module.py) it will be the main and
# the if block will execute
# This can be used to prevent code in another module from running when it is loaded
# Enables us to have a module that can run as a program itself
# And also be imported without running it's code unless we call the funcs ourselves




# https://docs.python-guide.org/writing/structure/
# Repository structure is important
# Recommended struct:
README.rst
LICENSE
setup.py
requirements.txt
sample/__init__.py
sample/core.py
sample/helpers.py
docs/conf.py
docs/index.rst
tests/test_basic.py
tests/test_advanced.py
# TODO breakdown info

# Decorators - replace undecorated function without overriding it
# Context Managers
with open('file.txt') as f:
    contents = f.read()
# using with ensures the file gets opened and closed
# Can implement this myself two different ways
class CustomOpen(object):
    def __init__(self, filename):
        self.file = open(filename)

    def __enter__(self):
        return self.file

    def __exit__(self, ctx_type, ctx_value, ctx_traceback):
        self.file.close()

with CustomOpen('file') as f:
    contents = f.read()
# whatever enter returns is assigned to f 
# exit method is called once with block finishes executing

# using a generator
from contextlib import contextmanager

@contextmanager
def custom_open(filename):
    f = open(filename)
    try:
        yield f
    finally:
        f.close()

with custom_open('file') as f:
    contents = f.read()

# Options for concatenated strings from bad to best
# create a concatenated string from 0 to 19 (e.g. "012..1819")
nums = ""
for n in range(20):
    nums += str(n)   # slow and inefficient
print nums

# create a concatenated string from 0 to 19 (e.g. "012..1819")
nums = []
for n in range(20):
    nums.append(str(n))
print "".join(nums)  # much more efficient

# create a concatenated string from 0 to 19 (e.g. "012..1819")
nums = [str(n) for n in range(20)]
print "".join(nums)

# create a concatenated string from 0 to 19 (e.g. "012..1819")
nums = map(str, range(20))
print "".join(nums)

# some string things
foo = 'foo'
bar = 'bar'

foobar = foo + bar  # This is good
foo += 'ooo'  # This is bad, instead you should do:
foo = ''.join([foo, 'ooo'])




# List comprehensions
# https://www.pythonforbeginners.com/lists/list-comprehensions-in-python/
# Old way
new_list = []
for i in old_list:
    if filter(i):
        new_list.append(expressions(i))
# New way
new_list = [expression(i) for i in old_list if filter(i)]

# Some useful samples
squares = [x**2 for x in range(10)] # squares 1-9
[x.lower() for x in ["A","B","C"] # returns a, b, c

string = "Hello 12345 World"
numbers = [x for x in string if x.isdigit()] # returns ['1','2','3','4','5']

fh = open("test.txt", "r")
result = [i for i in fh if "line3" in i] # prints the entire line containing line3

def double(x):
  return x*2
[double(x) for x in range(10)] # returns [0,2,4,6....18]

[x+y for x in [10,30,50] for y in [20,40,60]] # adds 1st x to each y, then 2nd x to each y...
#[30, 50, 70, 50, 70, 90, 70, 90, 110]



# Mutable vs Immutable Objects in Python
# https://medium.com/@meghamohan/mutable-and-immutable-side-of-python-c2145cf72747

# immutable: bool, int, float, tuple, str, frozenset, complex, bytes
# mutable: list, set, dict, bytearray

# id() returns identity of obj as int = loc in memory
# is compares identity of two objs
# type() returns type of obj
''' Example 1 '''
>>> x = "Holberton"
>>> y = "Holberton"
>>> id(x)
140135852055856
>>> id(y)
140135852055856
>>> print(x is y) '''comparing the types'''
True

''' Example 2 '''
>>> a = 50
>>> type(a)
<class: ‘int’>
>>> b = "Holberton"
>>> type(b)
<class: 'string'>

# immutable objects: changing an obj e.g. x = x + 1 creates a new obj
# the obj can't be changed so a new one has to be created, new ID
# mutable objects: popping an item from a list doesn't change the obj ID. 
# List contents change, list still points to same place, same ID

# immutable quicker to access but expensive to "change"

# a tuple is immutable but the values of it's objects can change
# e.g. a list inside a tuple can have it's contents changed
# the bindings are unchangeable but the objects themselves are not

# functions
# can call objs by reference
# e.g. send in a list, add to that list, list updates
def updateList(list1):
    list1 += [10]

n = [5, 6]
print(id(n))                  # 140312184155336
updateList(n)
print(n)                      # [5, 6, 10]
print(id(n))                  # 140312184155336

# or can call objs by pass by value
# e.g. send in a number, number is used for something but og num isn't modified
def updateNumber(n):
    print(id(n))
    n += 10

b = 5
print(id(b))                   # 10055680
updateNumber(b)                # 10055680
print(b)                       # 5



