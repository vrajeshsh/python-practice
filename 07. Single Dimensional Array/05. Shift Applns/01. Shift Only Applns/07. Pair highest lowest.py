import os
os.system("cls")

print("To pair the highest and lowest integers together:")
n = int(input("Enter number of inetgers: "))
print()

nums, start = [], 0

for i in range(n):
    print("Enter element #",i+1,": ",sep='', end='')
    nums.append(int(input()))

print("\nOriginal array:\n",nums, sep='')

while start < n:
    nums.insert(start, nums.pop(nums.index(max(nums[start:]))))
    start+=1
    if start==n:
        break
    nums.insert(start, nums.pop(nums.index(min(nums[start:]))))
    start+=1

print("\nRearranged array:\n",nums, sep='')
