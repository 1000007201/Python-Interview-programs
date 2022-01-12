# Python program to check a number is prime or not

temp,i = 0,0

n = int(input("Enter number to be checked "))
for i in range(2,n//2):
    if n % i == 0:
        temp = 1
        break
if temp==1:
    print("The number is not Prime")

else:
    print("The number is Prime")