'''
Ask the user for a number and determine whether the number is prime or not. 
(For those who have forgotten, a prime number is a number that has no divisors.).
'''

def isPrime(x):
    if num < 2:
        return False
    
    
    for divisors in range (2, int(num/2)):     
        if(num % divisors == 0):
            return False
        
    return True

num = input("Please enter a number ")
num = int(num)

if isPrime(num):
    print("Number is prime")
else:
    print("Number is not prime")


        
                

    
    



    