import os
os.system("cls")

print("To calculate the maximum subsequence in an array:")
n = int(input("Enter number of elements: "))
print()

nums = []
for i in range(n):
    print("Enter element #", i+1,": ", sep='', end='')
    nums.append(int(input()))

lgt, prev_max = len(nums), nums[0]
for i in range(1, lgt):
    maxi = max(prev_max, prev_max+nums[i])
    prev_max = maxi

print(prev_max)
