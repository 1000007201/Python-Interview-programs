# Python program to find sum of digits by reccursion

def sumDigit(num):
    if num==0:
        return num
    else:
        return n%10 + sumDigit(n//10)

n = int(input("Enter number "))
sum = sumDigit(n)
print(f"Sum of digits is {sum}")

