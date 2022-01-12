# Python program to find most repeated alements in an array

arr,occ = [],[]
n = int(input("Enter number of elements in array: "))
for x in range(n):
    occ.append(0)

for i in range(n):
    element = int(input(f"Enter element of an array between 1-{n-1}: "))
    arr.append(element)
    occ[arr[i]] = occ[arr[i]] + 1
for i in range(n):
    if occ[i]>1:
        print(f"{i} is repeated {occ[i]} times")
