lst = ["ram","karan","kumar","amit"]
result = []
for i in lst:
    temp = i.split()
    for ele in temp:
        if ele[0].lower() == "k":
            result.append(ele)
        
print(result)