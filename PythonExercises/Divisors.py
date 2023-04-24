user_number = int(input("Please enter a number"))

listRange = list(range(1,user_number + 1))

divisorList = []

for num in listRange:
    if user_number% num == 0:
        divisorList.append(num)
        
print(divisorList)


