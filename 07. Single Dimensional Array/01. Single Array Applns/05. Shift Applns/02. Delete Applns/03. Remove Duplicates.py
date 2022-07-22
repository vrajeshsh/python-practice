import os
os.system("cls")

print("To remove all duplicates elements from an array:")
n = int(input("Enter number of elements: "))
print()

nums= []
for i in range(n):
    print("Enter element #",i+1,": ", sep='',end='')
    nums.append(int(input()))

print("\nThe original array:\n", nums, sep='')

for i in range(n-1, -1, -1):
    if nums.count(nums[i]) > 1:
        nums.pop(i)

if n==len(nums):
    print("\nNo duplicate element found in the array!\n")
else:
    print("\nThe array after packing:\n", nums,"\n", sep='')
    
#You have a very 'RESTLESS' mind!!