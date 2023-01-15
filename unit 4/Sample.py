import re

# #Split a statement, based on single space
# txt = "The rain in Spain"
# x = re.split("\s", txt) # this will return a list of words
# print(x)

# #Control the number of occurences by specifying the maxsplit 
# txt = "The rain in Spain"
# x = re.split("\s",txt,1)
# print(x) 

txt =  "20.12.20ab I Hey this amit Chauhan, Software Engineer , amit.chauhan@gmail.com akash 12.12.2012 12122012"

# # @. * ReGex [+: one or more, *: zero or more]
# result = re.search("@.*", txt).group().split()[0]
# # print(result.group())
# print(result)

# [0-9]{2}\.[0-9]{2}\.[0-9]{4} ReGex
# result = re.search("[0-9]{2}\.[0-9]{2}\.[0-9]{4}", txt)
# result = re.findall("[0-9]{2}\.[0-9]{2}\.[0-9][0-9][a-z].", txt)
# print(result)
# # print(result.group())

#return all the words of a string that starts with vowel
# print(re.findall("\\b[aeiouAEIOU]\S+", txt))

# print(re.findall("Hel?y", txt))

# print(re.findall("^\d", txt))

# print(re.findall("H\w+", txt))