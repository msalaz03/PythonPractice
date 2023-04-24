'''
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
'''

str = input("Please enter a string ")
str_reverse = str[::-1]

if (str == str_reverse):
    print("Palidrome")
else:
    print("Not Palidrome")