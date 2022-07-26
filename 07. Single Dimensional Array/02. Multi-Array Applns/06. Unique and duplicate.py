import os
os.system("cls")

print("To separate unique and non-unique elements of an array:")
n = int(input("Enter number of elements: "))
print()

nums, uniques, non_unique = [], [], []
for i in range(n):
    print("Enter element #",i+1,": ",sep='', end='')
    nums.append(int(input()))

for i in range(n):
    if nums.count(nums[i])==1:
        uniques.append(nums[i])
    elif nums[i] not in non_unique:
        non_unique.append(nums[i])

print("\nOriginal array:\n", nums, 
    "\n\nUnique array elements:\n", uniques,
    "\n\nNon-Unique elements:\n",non_unique,"\n", sep='')
