import os
os.system("cls")

def isPrime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def nextPrime(n):
    n+= 1    
    while not isPrime(n):
        n+=1
    return n
    
print("Insert next Prime after each composite element of array:")
n = int(input("Enter number of elements: "))
print()

nums= []
for i in range(n):
    print("Enter element #",i+1,": ",sep='', end='')
    nums.append(int(input()))

print("\nThe original array:\n",nums,"\n", sep='')

i = len(nums)-1
while i >= 0:
    if not isPrime(nums[i]):
        nums.insert(i+1, nextPrime(nums[i]))
    i-=1

if n==len(nums):
    print("\nNo composite numbers present in the array!\n")
else:
    print("\nArray elements after inserting next prime integers after the composite ones:\n",
            nums,"\n", sep='')