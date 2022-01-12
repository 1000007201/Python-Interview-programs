# Python program to find two largest number in an array
import array
arr = []
n = int(input("Enter length of an array: "))
for i in range(n):
    element = int(input("Enter value of element: "))
    arr.append(element)

sorted_array = sorted(array.array('i',arr))
for i in range(len(arr)-1,0,-1):
    if sorted_array[i] != sorted_array[i-1]:
        print(f"Two largest numbers are {sorted_array[i-1]} and {sorted_array[i]}")
        break
