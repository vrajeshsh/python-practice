import os
os.system("cls")

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num**.5)+1):
        if num%i==0:
            return False
    return True

start = int(input("Enter starting limit: "))
end = int(input("Enter ending limit: "))

primeFib= ""

for i in range(start, end+1, 2):
    a, b, ssum = 1, 1, 0 
    while ssum<i:
        ssum = a + b
        a, b = b, ssum
    if ssum==i and isPrime(i):
        primeFib+= str(i) if primeFib=="" else ", "+str(i)

print("\nPrime Fibonacci numbers present between",start,"and",end,"are:\n",primeFib,"\n")
