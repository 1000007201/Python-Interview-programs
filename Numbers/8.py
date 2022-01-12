# Python program to find greatest among three numbers

n1 = int(input("Enter First number"))
n2 = int(input("Enter Second number"))
n3 = int(input("Enter Third number"))

if n1>n2 and n1>n3:
    print(f"{n1} is greatest")
elif n2>n1 and n2>n3:
    print(f"{n2} is greatest")
elif n3>n2 and n3>n1:
    print(f"{n3} is greatest")