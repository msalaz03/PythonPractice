def Fibonacci(count):
    
    i = 1
    if count == 0:
        fib = []
    elif count == 1:
        fib = [1]
    elif count == 2:
        fib = [1,1]
    elif count > 2:
        fib = [1,1]
        while i < (count - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1

    return fib
   
#Recursive but doesn't work for big numbers.   
def fib(n):
    
    if (n<=2): 
        return 1
    return fib(n - 1) + fib(n - 2)


#print(fib(8))
print(Fibonacci(50))

        
