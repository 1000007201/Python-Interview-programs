# Check this number is armstrong number or not

n = int(input("Enter to be checked:"))
x = 0
temp = n
while n!=0:
    x = x + (n%10)**3
    n = n//10

if temp==x:
    print(f"Your number is armstrong number")

else:
    print("Your number is not armstrong number")



    