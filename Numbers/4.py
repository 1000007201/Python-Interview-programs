# Python program to print fibonacci series by iterative method

first,second = 0,1

n = int(input("Enter number of terms to be printed"))
for i in range(0,n):
    if i<=1:
        result = i
    else:
        result = first + second
        first = second
        second = result
    print(result)

