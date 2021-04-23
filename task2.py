#fibonacci series

#fib(n)=fib(n-1)+fib(n-2)
def fibonacci(n):
 if n<0:
    print("Enter a positive value")
 elif n==0:
    return 0
 elif n==1:
    return 1
 else:
    return fibonacci(n-1)+fibonacci(n-2)
    
n=int(input("Enter the input "))
for i in range(n):
    print(fibonacci(i))
