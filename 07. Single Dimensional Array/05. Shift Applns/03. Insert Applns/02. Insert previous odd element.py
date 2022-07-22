import os
os.system("cls")

print("Insert previous odd numbers before each even element in array:")
n = int(input("Enter number of elemets: "))
print()

nums= []
for i in range(n):
    print("Enter element #",i+1,": ",sep='', end='')
    nums.append(int(input()))

print("\nThe original array:\n",nums,"\n", sep='')

i = len(nums)-1
while i >= 0:
    if nums[i]%2==0:
        nums.insert(i, nums[i]-1)
        i-=1
    i-=1

if n==len(nums):
    print("\nNo even numbers present in the array!\n")
else:
    print("\nArray elements after inserting previous odd integers before the even ones:\n",
            nums,"\n", sep='')