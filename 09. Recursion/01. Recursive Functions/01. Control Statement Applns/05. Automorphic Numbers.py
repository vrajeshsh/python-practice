import os
os.system("cls")

def digitcount(n):
    return 0 if n==0 else 1+digitcount(n//10)

print("To check whether or not an integer is an automorphic number:")
n = int(input("Enter a number: "))

print("\n",n," is",""if n==(n*n)%(10**digitcount(n)) else " NOT"," an automorphic number.\n", sep='')
