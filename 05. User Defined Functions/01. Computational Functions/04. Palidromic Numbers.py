import os
os.system("cls")

def getReverse(num):
    rev = 0
    while num > 0:
        rev = (rev*10)+num%10
        num//=10
    return rev

print("To check Palidrome:")
num = int(input("Enter a number: "))

print("\n", num, "is", "" if num==getReverse(num) else "NOT",
    "Palindromic\n")