import os
os.system("cls")

def isPrime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

print("To remove all prime elements from an array:")
n = int(input("Enter number of elements: "))
print()

nums = [] 
for i in range(n):
    print("Enter element #",i+1,": ", sep='',end='')
    nums.append(int(input()))

print("\nThe original array:\n", nums, sep='')

i = n-1
while i>=0:
    if isPrime(nums[i]):
        nums.remove(nums[i])
    i-=1

print(nums)
