#---------- FOR LOOP---------------

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# --------LOOPING THROUGH A STRING-----------

for x in "banana":
  print(x)

# --------------BREAK STATEMENT-------------

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

# -------------CONTINUE STATEMENT------------

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

# ------------RANGE() FUNCTION----------------

for x in range(6):
  print(x)

#----------- ELSE IN FOR LOOP----------------

for x in range(6):
  print(x)
else:
  print("Finally finished!")

# ------------NESTED LOOPS-------------------

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

# --------------PASS STATEMENT----------------

for x in [0, 1, 2]:
  pass