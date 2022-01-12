# Python program to find missing number.If 1-100 numbers are stored in an array.

arr = []
n = int(input("Enter length of an array: "))
for i in range(n-1):
    x = int(input("Enter value of an element: "))
    arr.append(x)
sum = (n*(n+1))/2
sumarr = 0
for i in range(n-1):
    sumarr = sumarr + arr[i]

print(f"Missing element in an array: {int(sum - sumarr)}")

