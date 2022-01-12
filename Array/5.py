# Python program to find second largest element in an array

import array
arr = []
n = int(input("enter size of array : "))
for x in range(n):
    x=int(input("enter element of array : "))
    arr.append(x)
 
sorted_array = sorted(array.array('i', arr))
for i in range(len(arr)-1, 0, -1):
    if sorted_array[i]!=sorted_array[i-1]:
        print(f"second largest element is {sorted_array[i-1]}")
        break 