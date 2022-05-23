import os
os.system("cls")

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num**.5)+1):
        if num%i==0:
            return False
    return True

primefacs=""
num = int(input("Enter an integer to generate its Prime Factors: "))

for i in range(2, int(num**.5)+1):
    if num%i==0 and isPrime(i):
        primefacs+= str(i) if primefacs=="" else ", "+str(i)

print("\nPrime Factors of",num,"are:\n",primefacs,"\n")