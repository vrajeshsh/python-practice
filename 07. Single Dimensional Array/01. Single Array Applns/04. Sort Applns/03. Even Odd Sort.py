import os
os.system("cls")

print("Sort even and odd separately in Ascending order:")
n = int(input("Enter number of elements: "))
print()

nums, even, odd = [], [], []
for i in range(n):
    print("Enter element #",i+1,": ",sep='', end='')
    nums.append(int(input()))
    if nums[i]%2:
        odd.append(nums[i])
    else:
        even.append(nums[i])

print("\nThe array:\n",nums,sep='')

nums = sorted(even)+sorted(odd)

print("\nArray after sorting even and odd elements separately:\n",
        nums,"\n",sep='')