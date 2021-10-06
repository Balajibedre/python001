# ----------CLASS--------

class MyClass:
  x = 5

#---------CRIATE OBJECT------

p1 = MyClass()
print(p1.x)

#--------The __init__() Function------

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

#--------OBJECT METHOD-------

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

#------- THE SELF PARAMITER-------

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

#--------MODIFY OBJECT PROPERTICES--------

p1.age = 40

#-------DELETE OBJECT PROPERTICES--------

del p1.age

#-------DELETE OBJECTS-------

del p1

#------THE PASS STATEMENT-----

class Person:
  pass
