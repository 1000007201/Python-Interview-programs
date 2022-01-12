# Pyhton program to check wheather a number is palindrome or not

n = int(input("Enter number to be checked"))
temp,rev = n,0

while temp != 0:
    rev = rev*10 + temp%10
    temp = temp//10

if rev == n:
    print("The number is pallindrome")

else:
    print("The number is not pallindrome")