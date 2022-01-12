# Python program to check wheather a number is pallindrom or not by reccursion

n = int(input("Enter number to be checked "))
def rev(num):
    if num<10:
        return num
    else:
        return int(str(num%10) + str(rev(num//10)))

def isPall(num):
    if num == rev(num):
        return 1
    return 0

if isPall(n) == 1:
    print("Given number is pallindrome")

else:
    print("Given number is not pallindrome")