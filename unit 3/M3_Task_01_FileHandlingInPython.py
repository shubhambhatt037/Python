import os
path = os.path.dirname(__file__)
print(path)
path=path+'/'

file=open(path+'abc.text','r')
for each in file:
    print(each)

# various modes of opening a file

path='C:\\Users\\Dell 5000\\python workspace\\unit 3'
path = path + '/'
#write into a file

# file=open(path + 'abc.text','w')
# file.write("this is the write command ")
# file.write("it allows us to write in a particular file")
# file.close()

# Append mode(a mode)
file=open(path+'abc.text','a')
file.write(" hello")
file.write(" there!")
file.close()

file=open(path + 'abc.text','r')
print(file.read())

# Append mode(a+ mode)
file=open(path+'abc.text','a+')
file.write(" hello")
file.write(" there!")
file.seek(0)
print(file.read())

# split() lines
'''
-We can alose split lines using file handling in python.
 It splits the file data whem=n space is encountered.
-You can also split using any charaters as you wish'''

path='C:\\Users\\Dell 5000\\python workspace\\unit 3'
path = path + '/'
#file = open(path + 'abc.text'.'r')
with open(path+'abc.text','r') as file:
    data=file.readlines()
    for line in data:
        word=line.split() #line.split('a')
        print(word)
    
# readlines() method is used to read all the lines in the file
# readline() method only reads a line from the file

path='C:\\Users\\Dell 5000\\python workspace\\unit 3'
path = path + '/'

# # renaming a file
# import os
# os.rename(path+"ABC.text",path+"abc123.txt")

# # deleting a file
# os.remove(path+"ABC.text")