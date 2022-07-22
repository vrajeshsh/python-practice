import os
os.system("cls")

def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

print("To segragate prime and composite elements of an array: ")
n = int(input("Enter number of elements: "))
print()

nums, primes, composites, others = [], [], [], []

for i in range(n):
    print("Enter element #",i+1,": ",sep='', end='')
    nums.append(int(input()))
    if nums[i]<2:
        others.append(nums[i])
    elif isPrime(nums[i]):
        primes.append(nums[i])
    else:
        composites.append(nums[i])

print("\nOriginal Array:\n",nums, sep='')
if primes==[]:
    print("\nNo Prime elements exist in array!\n")
else:
    print("\nprime[] = ", primes)
if composites==[]:
    print("\nNo Composite elements exist in array!\n")
else:
    print("composites[] = ", composites)
if others==[]:
    print("\nNo left-over elements exist in array!\n")
else:
    print("leftover[] = ", others)
print()