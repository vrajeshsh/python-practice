import os
os.system("cls")

def isPrime(num):   # Internet code! Liked it very much so much that readily SACRIFICED what this old man had done here!!
    if num<2:
        return False
    for i in range(2, int(num**.5)+1):
        if num%i==0:
            return False
    return True

num = int(input("Enter an integer to check for prime number: "))
if isPrime(num):
    print("\nThe integer",num,"is a Prime!\n")
else:
    print("\nThe integer",num,"is NOT Prime!\n")
