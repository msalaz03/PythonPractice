a = [1,2,3,4,5,6]
# b = [number for number in a if number % 2 == 0]


for num in a:
    if(num % 2 != 0):
        a.remove(num)
        
print(a)
#print(b)