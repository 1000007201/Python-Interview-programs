# Python program to check two strings are anagram

s1 = input("Enter String 1: ")
s2 = input("Enter String 2: ")

def anagam(s_1,s_2):
    if (sorted(s_1)==sorted(s_2)):
        return True
    else:
        return False

if anagam(s1,s2):
    print("Anagam")

else:
    print("Not Anagam")