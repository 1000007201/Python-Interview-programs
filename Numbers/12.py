# Python program to check number is perfect or not
# Perfect Number is defined as number equal to sum of its divisors excluding itself
# eg.: 6 is a perfect number 1+2+3 = 6

n = int(input("Enter number to be checked  "))
sum = 0
for i in range(1,(n//2)+1):
    if n%i==0:
        sum = sum + i
if sum == n:
    print("Your number is a perfect number")

else:
    print("Your number is not perfect number")

