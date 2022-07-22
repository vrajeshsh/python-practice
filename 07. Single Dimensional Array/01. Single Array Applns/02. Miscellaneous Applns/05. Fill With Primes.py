import os
os.system("cls")

def isprime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

primes = []
print("To display all Prime numbers uptil 'n':")
n = int(input("Enter the ending limit: "))

for i in range(2, n):
    if isprime(i):
        primes.append(i)

print("\nAll Prime numbers upto ",n," are:\n", primes,"\n", sep='')