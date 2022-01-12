# Program to reverse an integer

n = int(input("Enter Number to be reversed: "))
print(f"Number before reverse:{n}")
rev = 0
while n!=0:
    rev = rev*10 + n%10
    n = n//10
print(f"Your reverse number is : {rev}")