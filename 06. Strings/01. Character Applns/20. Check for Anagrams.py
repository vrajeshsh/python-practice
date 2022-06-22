import os
os.system("cls")

def stringSort(str):
    new_str=""
    for i in range(65, 91): # generating the ASCII values for 'A' till 'Z' here
        ch= chr(i)
        for j in str:
            if ch==j.upper():
                new_str+= ch
    return new_str

print("To check Anagrams:\n")
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

print("\nStrings are","" 
    if stringSort(str1)==stringSort(str2) else " NOT",
    " anagrams!\n", sep='')
