# Python program to check given string is pallindrome or not

n = input("Enter String to be checked: ")

if n == n[::-1]:
    print("String is pallindrome")

else:
    print("String is not pallindrome")