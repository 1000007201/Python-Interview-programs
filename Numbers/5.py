# Python program to print fibonacci series using Recursion

n = int(input("Enter number of terms to be printed"))

def fib(num):
    if num==0:
        return 0

    elif num == 1:
        return 1

    else:
        return fib(num-2)+fib(num-1)

for i in range(0,n):
    print(fib(i))
