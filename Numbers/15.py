# Python program to find sum of digits by using string

n = input("Enter number ")
sum =0

for i in n:
    sum = sum + int(i)

print(f"Sum is {sum}")
