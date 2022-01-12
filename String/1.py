# Python Program to count the occurrence of given character in a string

n = input("Enter String: ")
char = input("Enter Character to be searched")
count = 0

for i in range(len(n)):
    if n[i]==char:
        count +=1
print(f"{count} number of occurence of {char}")