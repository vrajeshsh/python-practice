import os
os.system("cls")

print("To find the most occuring duplicating element (mode) of an array of integers:")
n = int(input("Enter number of elements: "))
print()

nums, mode, max_cnt = [], 0, 0
for i in range(n):
    print("Enter element #", i+1,": ", sep='', end='')
    nums.append(int(input()))

lgt = len(nums)
for i in range(lgt):
    count = nums.count(nums[i])
    if count >= max_cnt:
        max_cnt = count
        mode = nums[i] if mode < nums[i] else mode

print("\nThe given array of integers:\n", nums,
    "\nMODE of the array: ",mode,"\n",sep='')
