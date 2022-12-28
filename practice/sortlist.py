lst = [1,2,3,4,5]

flag = 0

# if(lst == sorted(lst)):
#     flag=1

# if flag == 1:
#     print("List is sorted")
# else:
#     print("List is not sorted")

if sorted(lst) == lst:
    print("Ascending")
elif sorted(lst,reverse = True) == lst:
    print("Descending")
else:
    print("Not sorted")