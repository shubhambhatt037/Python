# a = input("Enter a character-> ")
# if a.lower()=='a' or a.lower()=='e' or a.lower()=='i' or a.lower()=='o' or a.lower()=='u':
#     print("Vowel")
# else:
#     print("Consonant")

# a = int(input("Enter a number-> "))
# sum = 0
# for i in str(a):
#     sum += int(i)

# print(sum)

# lst = [1,2,3,4,5]
# result = []
# for i in range(0,len(lst)):
#     if lst[i]%2 == 0:
#         result.append(lst[i])

# print(result)

# stack = [1,2]
# op = input("Enter operation you want to perform-> ")
# match op:
#     case 'a':
#         x = input("Enter element you want to insert - >")
#         stack.append(x)
#         print(stack)
#     case 'b':
#         stack.pop()
#         print(stack)
#     case 'c':
#         print(stack)

x = int(input("Enter a number-> "))
sumO=0
sumE=0
t=0
for i in range(0,x):
    if t%2 ==0:
        sumE = sumE + t
    else:
        sumO = sumO + t 
    t = t+1

print("Sum of odd ",sumO)
print("Sum of Even ",sumE)