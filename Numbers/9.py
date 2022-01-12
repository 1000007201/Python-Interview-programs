# Python program to check given number is binary or not

n = int(input("Enter number to be checked"))

while n!=0:
    j = n%10
    if j!=0 and j!=1:
        print("The number is not Binary")
        break
    n = n//10
if n == 0:
    print("The number is Binary")
    