import os
os.system("cls")

def isPrime(num):
    if num<2:
        return False
    for i in range(2, int(num**.5)+1):
        if num%i==0:
            return False
    return True

num = int(input("Enter an integer to find the next and previous primes: "))

i, j = num+1, num-1
while not isPrime(i):
    i+=1
print("\nNext Prime after",num,"is",i)

if num > 2:
    while not isPrime(j):
        j-=1
    print("Previous Prime before",num,"is",j,"\n")    
else:
    print("\nNo previous prime exists before",num,"!\n")
