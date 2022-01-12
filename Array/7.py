# Python program to remove duplicate elements from an array

arr,count = [],[]

n = int(input("Enter length of an array: "))

for i in range(n):
    count.append(0)
    element = int(input(f"Enter value of element between 0 - {n-1}: "))
    arr.append(element)

for i in range(n):
    count[arr[i]] = count[arr[i]] + 1
    if count[arr[i]] == 1:
        print(arr[i])