import os
os.system("cls")

def remainder(num, den):
    return num if num<den else remainder(num-den, den)

print("To check whether a number is divisible by 11:")
n = int(input("Enter a number: "))

print("\n",n," is","" if remainder(n,11)==0 else " NOT"," divisible by 11.\n", sep='') 
