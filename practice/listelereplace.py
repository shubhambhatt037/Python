num = [45,22,14,65,97,72]


for i in range(0,len(num)):
    if num[i]%3 == 0 and num[i]%5 != 0:
        num[i] = "ppp"
    elif num[i]%5 ==0 and num[i]%3 !=0 :
        num[i] = "qqq"
    elif num[i]%5 ==0 and num[i]%3 ==0:
        num[i] = "pppqqq"

print(num)
