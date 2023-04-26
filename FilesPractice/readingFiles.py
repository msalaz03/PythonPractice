
employee_file = open("employees.txt", "r")

#print(employee_file.readlines()[1])
# print(employee_file.readline())

for employee in employee_file.readlines():
    print(employee)



employee_file.close()

 



