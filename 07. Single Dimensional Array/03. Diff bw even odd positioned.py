import os
os.system("cls")

nums, odd, even = [], 0, 0
print("To find the difference between even and odd positioned elements:")
n = int(input("Enter number of elements: "))
print()

for i in range(n):
    print("Enter element #",i+1,": ",sep='', end='')
    nums.append(int(input()))

for i in range(len(nums)):
    if (i+1)%2==1:
        odd+=nums[i]
    else:
        even+=nums[i]
diff = even-odd

print("\nThe array:\n", nums,
    "\n\nDifference between even and odd positioned elements: ",
    diff,"\n", sep='')