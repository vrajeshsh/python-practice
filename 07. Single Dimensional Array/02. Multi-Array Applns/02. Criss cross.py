import os
os.system("cls")

print("To move 1st element in first array to second position and vice versa:")
n = int(input("Enter number of elements: "))
print()

nums, nums2 = [], [0]*n

for i in range(n):
    print("Enter element #",i+1,": ",sep='', end='')
    nums.append(int(input()))

i = 0
nums2[n-1] = nums[n-1]
while i < n-1:
    nums2[i+1] = nums[i]
    nums2[i] = nums[i+1]
    i+= 2

print("\nThe original array:\n",nums,
    "\n\nThe array after criss-cross copy:\n",nums2,"\n", sep='')
