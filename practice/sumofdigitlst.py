lst = [24,45,37,28,19]

result = []
for i in lst:
    sum =0
    for d in str(i):
        sum += int(d)
    result.append(sum)

print("The result is ",result)

