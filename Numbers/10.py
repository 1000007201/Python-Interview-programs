# Python program to swap two numbers without using third variable

a = int(input("Enter first number"))
b = int(input("Enter second number"))

a = a-b
b = a+b
a = b-a

print("After Swapping:")
print(f"First variable {a}")
print(f"Second variable {b}")
