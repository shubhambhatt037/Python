# Inheritance and multiple Inheritance in Python

class Class1:
    def display(self):
        print("In Class1")


class Class2(Class1):
    def display(self):
        print("In Class2")


class Class3(Class1):
    def display(self):
        print("In Class3")


class Class4(Class2, Class3):
    pass


obj = Class4()
obj.display()


# Polymorphism
'''
- The word polymorphism means having many forms.
- In programming, polymorphism means the same
  function name(but different signatures) being used for 
  different types.
- The key difference is the data types and number of 
  arguments used in function.

1. Inbuilt polymorphic functions
    print(len("Akash"))
    print(len([10, 20, 30]))

2. User-defined polymorphic functions
    def add(x, y, z = 0):
        return x + y + z

    print(add(2,3))
    print(add(2,3,4))
'''


class India():
    def capital(self, a = None):
        if a:
            print(a + " is the capital of India")
        else:
            print("New Delhi is the capital of India")

    def language(self):
        print("Hindi is the most widely spoken language in India")

obj_ind = India()
obj_ind.capital("New Delhi") # New Delhi is the capital of India

obj_ind = India()
obj_ind.capital() # New Delhi is the capital of India


# Method Overloading
####################


def add(datatype, *args):
    if datatype == 'int':
        answer = 0

    if datatype == 'str':
        answer = ''

    for x in args:
        answer = answer + x

    print(answer)


# Integer
add('int', 5, 6)

# Strings
add('str', 'Hi', 'Geeks')

# Method Overriding
###################


class A:
    def fun1(self):
        print('Fun1 of class A')

    def fun2(self):
        print('fun2 of class A')

class B(A):
    def fun1(self):
        print('Fun1 of class B')
        
    def fun2(self):
        print('fun2 of class B')
        super().fun2()

# Create an object of class B
b = B()
b.fun1() # Output: Fun1 of class B
b.fun2() # Output: fun2 of class B, fun2 of class A

# Data Hiding
'''
In Python, data hiding is achieved by using a naming convention where member variable
or method names are preceded by a double underscore (__) character. This causes the 
Python interpreter to replace the name of the member with a modified version of the name.
For example, if a member variable is named __x, the interpreter will replace it 
with _classname__x where classname is the name of the class. This makes the variable 
difficult to access from outside the class, but not completely inaccessible.
'''
class MyClass:
    def __init__(self):
        self.__x = 0

    def get_x(self):
        return self.__x

    def set_x(self, value):
        self.__x = value

obj = MyClass()
print(obj.get_x()) # Output: 0
obj.set_x(10)
print(obj.get_x()) # Output: 10

# This will raise an AttributeError
try:
    print(obj.__x)
except AttributeError as e:
    print(e)
