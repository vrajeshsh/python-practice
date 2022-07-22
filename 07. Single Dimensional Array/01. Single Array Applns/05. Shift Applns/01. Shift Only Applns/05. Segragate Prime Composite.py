import os
os.system("cls")

def isPrime(n):
    if n<2:
        return False
    for i in range(2, n//2+1):
        if n%i==0:
            return False
    return True

print("To shift the Prime digits to the left and composite to the right:")
n = int(input("Enter number of integers: "))
print()

nums, start = [], 0
for i in range(n):
    print("Enter element #",i+1,": ",sep='', end='')
    nums.append(int(input()))

print("\nThe original array:\n", nums, sep='')

for i in range(n):
    if isPrime(nums[i]):
        nums.insert(start, nums.pop(i))
        start+=1
    elif nums[i]<2:
        nums.insert(start, nums.pop(i))

print("\nThe array after shifting Prime digits to the left and composite to the right:\n",nums,sep='')

