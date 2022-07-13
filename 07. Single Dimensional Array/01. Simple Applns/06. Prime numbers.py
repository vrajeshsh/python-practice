import os
os.system("cls")

def isprime(num):
    if num<2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            return False
    return True

nums, primes=[], ""
print("To display all prime numbers present in an array:")
n = int(input("Enter number of elements: "))
print()

for i in range(n):
    print("Enter element #", i+1,": ", sep='', end='')
    nums.append(int(input()))
    if isprime(nums[i]):
        primes+=str(nums[i]) if primes=="" else ", "+str(nums[i])

print("The array:\n",nums,sep='')
if primes=="":
    print("\nNo prime numbers present in the array!\n")
else:
    print("\nPrime numbers present in the array: ", primes,"\n", sep='')