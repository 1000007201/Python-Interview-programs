# Python program to find sum of digits

n = int(input("Enter number "))
sum = 0

while n!=0:
    sum = sum + n%10
    n = n//10

print(f"Sum is {sum}")