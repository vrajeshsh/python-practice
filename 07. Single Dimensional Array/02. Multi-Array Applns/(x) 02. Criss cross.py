import os
os.system("cls")

print("To move 1st element in first array to second position and vice versa:")
n = int(input("Enter number of elements: "))
print()

nums, nums2 = [], [0]*n
for i in range(n):
    print("Enter element #",i+1,": ",sep='', end='')
    nums.append(int(input()))
    #nums[i] = nums2[i-1] if i%2 else nums2[i+1]

    #nums2[]= nums[i]

print("\nThe original array:\n",nums,
    "\n\nThe array after interchanging values:\n",nums2,"\n", sep='')

# Can you make this a check-less venture?