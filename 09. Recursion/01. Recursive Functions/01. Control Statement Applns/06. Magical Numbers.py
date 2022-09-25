import os
os.system("cls")

def digitsum(n):
    return 0 if n==0 else n%10+digitsum(n//10)

def ismagical(n): 
    if n == 1:
        return True
    elif n < 10:
        return False
    return ismagical(digitsum(n))

print("To check whether a number is Magical or not:")
n = int(input("Enter a number: "))

print("\n",n," is","" if ismagical(n) else " NOT"," a magical number.\n", sep='') 
