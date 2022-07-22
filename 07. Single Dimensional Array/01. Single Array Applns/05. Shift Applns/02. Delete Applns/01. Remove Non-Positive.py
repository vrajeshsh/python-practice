import os
os.system("cls")

print("To remove all non-positive elements from an array:")
n = int(input("Enter number of elements: "))
print()

nums= []
for i in range(n):
    print("Enter element #",i+1,": ", sep='',end='')
    nums.append(int(input()))

print("\nThe original array:\n", nums, sep='')

i= 0
while i < len(nums):
    if nums[i] <= 0:
        nums.pop(i)
        i-=1
    i+= 1

if n==len(nums):
    print("\nNo Non-Positive elements found in the array!\n")
else:
    print("\nThe array after removing non-positive elements:\n",nums,"\n", sep='')

# Version #1: Deletion with pop()
# i= n-1
# while i >= 0:
#     if nums[i] <= 0:
#         nums.pop(i)
#     i-= 1

# Version #2: Deletion with remove():
# for i in range(n-1, -1, -1):
#     if nums[i] <= 0:
#         nums.remove(nums[i])
