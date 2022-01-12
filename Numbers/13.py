# Python program to find prime factors of any integer

n = int(input("Enter number to be checked  "))

for i in range(2,n+1):
    if n%i == 0:
        isPrime = 1
    for j in range(2,(i//2)+1):
        if i%j == 0:
            isPrime = 0

    if isPrime == 1:
        print(f"{i}")