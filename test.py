
days_of_week = {
    "Mon": "Monday",
    "Tues": "Tuesday",
    "Wed": "Wednesday",
    "Thurs": "Thursday",
    "Fri": "Friday"
    
}


key = input("What day of the week: ")

if key in days_of_week.keys():
    print(days_of_week[key])
else:
    print("Key not found.")

# b = 5
# c = 3

# # || = or
# # && = and

# if b > 0: 
#     print("test passed")
# elif c == 3:
#     print("c = 3")
# else:
#     print("test failed")
    
    
# for i in range(10):
#     print(i)
    
# ages = [10, 20, 15, 30, 40, 12]

# for d in ages:
#     print(d)
    
# while b > 0:
#     print(b)
#     b = int(input("Type a value for b"))
    
# def get_sum(a,b):
#     if isinstance(a, int) and isinstance(b, int):
#         return a + b
#     else:
#         print("Please enter a integer value")
        
# print (get_sum(5,10))
    