#Class Notes
# https://docs.python.org/3/tutorial/classes.html
# New Class creates new type of object
# Create instances of new object
# Instances have attributes attached to maintain state
# Can also have methods to modify state
# Can use multiple base classes, method can call method of base class, derived class
# 

'''multiple names (in multiple scopes) can be bound to same object (aliasing). Ignore when dealing with immutable types (numbers, string, tuples). Surprising when using mutable types (lists, dicts, most other types). Aliases behave like pointers. Passing an object passes the pointer. '''

# Namespace is a mapping from names to objects (ex. set of built in names, global names in module, local names, attributes of an objec). 
# No relation between names in differente name spaces. Created at different time (built in names created when Python starts, global namespace created when module definition read in, local namespace for function created when function called and deleted when it returns or raises exception that isn't handled in the function)

# z.real 
# real is an attribute of the object/module z
# Can write to attribute with 
# z.answer = 42
# can also delete with 
# del z.answer

# Scope is a textual region of Python where a namespace is directly accessible
# At least 3 nested scopes whos namespaces are directly accessible
''' 1. innermost scope, searched first, contains local names
2. scopes of any enclosing functions, which are searched starting with the nearest enclosing scope, contains non-local, but also non-global names
3. the next-to-last scope contains the current module's global names
4. the outermost scope (searched last) is the namespace containing built-in names'''

# if name is declared global then all refs and assignments go directly to global
# to rebind variables outside of innermost scope use nonlocal. If not declared nonlocal than read only and a new local var will be created.
# outside functions the local scope references same namespace as global scope. Class defs place another namespace in local scope.
# Scopes are determined textually - the global scope of a func defined in a module is that module's namespace

# if no global statement in effect than assignments to names always go to innermost scope
# assignments don't copy data - they just bind names to objects
# deletions removes the binding from the namespace

# global statement indicates that particular variable lives in global and should be rebound there
# nonlocal indicates that var lives in enclosing scope and should be rebound there

def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

''' output
After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spam'''

# CLass definitions like function definitions must be executed before they have any effect
# A new namespace is created and used as the local scope when a class defintion is entered
# When a class def is left, a class object is created which is a wrapper around the namespace contents
# Attribute references vs instantiation
# Attribute reference: obj.name
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

# attributes = MyClass.i and MyClass.f
# MyClass.i returns an integer, can change by assignment e.g. MyClass.i = 5
# MyClass.f returns a function boject
# MyClass.__doc__ is a valid attribute and returns """A simple example class"""
# x = MyClass() creates a new isntance of the class and assigns to local var x
# Use __init__ to instantiate class with certain state
def __init__(self):
    self.data = []
# initializes each instance to hold an empty array called data
# Below = example of passing values to initialize a certain state
>>> class Complex:
...     def __init__(self, realpart, imagpart):
...         self.r = realpart
...         self.i = imagpart
...
>>> x = Complex(3.0, -4.5)
>>> x.r, x.i
(3.0, -4.5)

# Instance objects have two attribute references - data attributes and methods
# data attributes are instance variables
# don't have to be declared, spring into existence when assigned to
# the following piece of code will print the value 16 without leaving a trace
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter

# Methods are functions that belong to object
# not unique to class - list objects have methods like append, insert, sort, etc.
# x.f is a valid method reference since MyClass.f is a function
# but x.i is not since MyClass.i is not
# But x.f is not the same thing as MyClass.f - it is a method obj, not a func obj
# Typically call a method right after it is bound
x.f()
# Can store away method object for use at later time
xf = x.f
while True:
	print(xf())
# Special thing about methods is that instance object is passed as first arg
x.f() == MyClass.f(x)
# a method attribute is created by packing pointers to instance obj and func obj into abstract obj aka method obj

# Class vs Instance variables
# instance = data unique to each instance
# class = data shared by all instances of class
class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.kind                  # shared by all dogs
'canine'
>>> e.kind                  # shared by all dogs
'canine'
>>> d.name                  # unique to d
'Fido'
>>> e.name                  # unique to e
'Buddy'

# Bad implemntation below - tricks should not be a class Var
class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks                # unexpectedly shared by all dogs
['roll over', 'play dead']

# Good implementation below - tricks is an instance var
class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks
['roll over']
>>> e.tricks
['play dead']

# Random Remarks
# data attributes override method attributes with same name
# solutions = capitalize method names, prefix data attrib with unique string (e.g. _), or using verbs for methods and nouns for data attributes
# data attribs may be refd by methods as well as ordinary users (clients) of an obj?
# classes are not usable to implement pure abstract data types?
# no data hiding ^?
# clients should use data attributes with care
# clients can add data attributes to instance obj without affecting validity of methods
# as long as name conflicts are avoided
# no shorthand for referencing data attributes/methods from within methods
# first argument is often self
# any function object that is a class attribute defines a method for instances of that class
# func def doesn't hav eto be in class def
# assigning a func obj to a local var is also ok
# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g

# Methods can call other methods using self
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)

# methods can ref global names
# global scope of a method is the module containing its def
# a class is never used as a global scope
# useful to use global scope to import funcs/modules
# Each val is an object and therefore has a class (type) store as object.__class__

# Inheritance
# syntax for derived class:
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>

# e.g
class DerivedClassName(modname.BaseClassName):

# if requested attribute is not found, base class(es) will be searched recursively
# derived classes can override methods of base class
# a method of a base calss that calls another method defined in same base class 
# may end up calling a method of a derived class that overrides it

# Multiple inheritance
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>

# searches depth first, left to right.
# aka searches Base1 recursively, then Base 2, then Base3

# Private variables
# private variables don't exist in Python
# convention: names prefixed with underscore (_spam) should be treated as non-public
# aka implementation detail subj to change without notice
# Can use "name mangling" to let subclass override method without breaking intraclass methods
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

# Odds and Ends
# an empty class can be used as a struct
class Employee:
    pass

john = Employee()  # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000

# code that expects particular abstract data type can be passed a class that emulates methods instead
# e.g. define read() and readline() that get data from a string buffer

# m.__self__ is the instance object with the method m()
# m.__func__ is func object corresponding to method

# Iterators
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line, end='')

# for statement calls iter() on container obj
# func returns iterator obj that defines method __next__()
# when no more elems next raises StopIteration exception that tells for loop to end
# Can call __next__() method using next()
>>> s = 'abc'
>>> it = iter(s)
>>> it
<iterator object at 0x00A1DB50>
>>> next(it)
'a'
>>> next(it)
'b'
>>> next(it)
'c'
>>> next(it)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    next(it)
StopIteration

# to add iteration to class add iter and next methods
# if class defines __next__() then __iter__() can return self
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

# Generators create iterators using the yield statement.
# Every time next is called the generator resumes where it left off
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

>>> for char in reverse('golf'):
...     print(char)
...
f
l
o
g

# generators are just compact iterators
# local vars and execution state are automatically saved between calls
# generators automatically raise StopIteration when they terminate

# Generator expressions
# designed for situations where generator is used right away by enclosing func
# more compact but less versatile than full generator def
# more memory friendly than equiv list comprehensions
>>> sum(i*i for i in range(10))                 # sum of squares
285

>>> xvec = [10, 20, 30]
>>> yvec = [7, 5, 3]
>>> sum(x*y for x,y in zip(xvec, yvec))         # dot product
260

>>> from math import pi, sin
>>> sine_table = {x: sin(x*pi/180) for x in range(0, 91)}

>>> unique_words = set(word  for line in page  for word in line.split())

>>> valedictorian = max((student.gpa, student.name) for student in graduates)

>>> data = 'golf'
>>> list(data[i] for i in range(len(data)-1, -1, -1))
['f', 'l', 'o', 'g']

