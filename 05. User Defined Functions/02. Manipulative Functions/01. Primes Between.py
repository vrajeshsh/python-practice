import os
os.system("cls")

def isPrime(num):
    if num<2:
        return False
    for i in range(2, int(num**.5)+1):
        if num%i==0:
            return False
    return True

primes=""
start = int(input("Enter starting limit: "))
end = int(input("Enter ending limit: "))

if start<=2  and end>2:
    primes="2"
    start=2
    if start%2==0:
        start+=1

for i in range(start, end+1, 2):
    if isPrime(i):
        primes+= str(i) if primes=="" else ", "+str(i)
    
print("\nPrime numbers present between",start,"and",end,"are:\n",primes,"\n")
