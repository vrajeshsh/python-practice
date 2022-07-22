import os
os.system("cls")

nums, maxi, sec_max, maxi_pos, sec_max_pos = [], 0, 0, -1, -1
print("To display the second highest element in the array:")
n = int(input("Enter the number if elements: "))
print()

for i in range(n):
    print("Enter element #", i+1,": ", sep='', end='')
    nums.append(int(input()))
    if nums[i]>maxi:
        sec_max = maxi
        sec_max_pos = maxi_pos
        maxi_pos = i
        maxi = nums[i]
    elif nums[i]>sec_max and nums[i]!=maxi:
        sec_max = nums[i]
        sec_max_pos = i
        
print("\nThe elements of the array:\n",nums,
    "\n\nThe second-highest element is ",sec_max,
    " occurring at position ",sec_max_pos+1,".\n", sep='')