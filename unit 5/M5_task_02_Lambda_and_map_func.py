# Lambda or anonymous functions in python
'''
- A Lambda function is a small anonymous function.
- A lambda function can take any number of arguments
- It can create functions in one line when possible
'''
def add(a, b):
    return a+b

def minus(x, y):
    return x-y-2


minus = lambda x, y: x-y
print(minus(9, 4))

# Q2. WAP in python to calculate the square root of a whole number by using lambda
# expression and math.sqrt technique

import math

root = lambda x: math.sqrt(x)
print(root(4))

# Map in python
'''
- The map() function executes a specified function for each item in an iterable
- The item us send to the function as a parameter.
'''

def myfunc(n):
    return len(n)
x = map(myfunc, ('apple','banana','cherry'))#,('orange','lemon','pineapple'))
print(list(x))

'''
Q3. WAP in python to check if the number is prime or not?
check multiple numbers at once
'''
import math
def primeornot(l):
    if l <=1:
        return "Not Prime"
    range_sqrt = math.sqrt(l)
    for i in range(2,int(range_sqrt) + 1):
        if l%i == 0:
            return "Not prime"
    return "Prime"

x = map(primeornot, (5,7,9,11))
print(list(x))
