
name = input("Please enter your name ")
age_str = input("Please enter your age ")

try:
    age = int (age_str)
    future_age = 2023 + (100 - age)
    print(f"Hi {name}, you will turn 100 years old in {future_age}.")
except ValueError:
    print("Invalid Input")
    

    

