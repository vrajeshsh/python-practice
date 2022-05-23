import os
os.system("cls")

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num**.5)+1):
        if num%i==0:
            return False
    return True

i, ssum, primes = 1, 0, ""

n = int(input("Enter number of numbers: "))

while i<=n:
    print("Enter number #",i,": ",end='', sep='')
    num = int(input())
    if isPrime(num):
        ssum+=num
        primes+= str(num) if primes=="" else ", "+str(num)
        print("Prime number '",num,"' found and has been added to sum!", sep='')
    i+=1

print("\nPrime numbers among the",n,"entered are:\n",primes,
    "\nSum of the numbers:",ssum,"\n")
