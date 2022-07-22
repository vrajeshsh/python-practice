import os
os.system("cls")

def sortorder(nums):
    n, asc_cnt, desc_cnt = len(nums), 0, 0

    for i in range(n-1):
        if nums[i]<=nums[i+1]:
            asc_cnt+=1
        if nums[i]>=nums[i+1]:
            desc_cnt+=1
    return 1 if asc_cnt==n-1 else 2 if desc_cnt==n-1 else 0

nums, asc_cnt, desc_cnt= [], 0, 0
print("To check if elements are arranged in ascending or descending order:\n")
n = int(input("Enter number of elements: "))
print()

for i in range(n):
    print("Enter element #", i+1,": ", sep='', end='')
    nums.append(int(input()))

print("\nThe elements of the given array:\n",nums, sep='')
order= sortorder(nums)
print("\nThe array is in ",
    "Ascending" if order==1 else \
    "Descending" if order==2 else \
    "No"," order\n", sep='')