# Python program to find the largest and smallest number in an array

arr = []
n = int(input("Enter number of elements in an array: "))
for i in range(n):
    element = int(input("Enter value of an element: "))
    arr.append(element)

largest = arr[0]
smallest = arr[0]
for i in range(n):
    if arr[i]>largest:
        largest = arr[i]
    if arr[i]<smallest:
        smallest = arr[i]

print(f"{largest} is greatest and {smallest} is smallest element in an array")