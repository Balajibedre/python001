####  TUPLE 

thistuple = ("apple", "banana", "cherry")
print(thistuple)

#### A tuple is a collection which is ordered and unchangeable.
#### Tuples are written with round brackets.
#### Tuple items are ordered, unchangeable, and allow duplicate values.
#### Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

#### DUPLICATE VALUES

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#### TUPLE LENGTH

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

####  TUPLE WITH ONE ITEM

#### One item tuple, remember the comma:

thistuple = ("apple",)
print(type(thistuple))

#### TUPLE ITEM DATA TYPE

tuple1 = ("apple", "banana", "cherry") # CHAR
tuple2 = (1, 5, 7, 9, 3)               # NUM
tuple3 = (True, False, False)          # BOOLEAN

####  A TUPLE WITH strings, integers and boolean values:

tuple1 = ("abc", 34, True, 40, "male")

####   Type() 
# <class 'tuple'>

####  The tuple() Constructor
####  It is also possible to use the tuple() constructor to make a tuple.
####  Using the tuple() method to make a tuple:

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#### Python Collections (Arrays)
## There are four collection data types in the Python programming language:

## List is a collection which is ordered and changeable. Allows duplicate members.
## Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
## Set is a collection which is unordered and unindexed. No duplicate members.
## Dictionary is a collection which is ordered* and changeable. No duplicate members.