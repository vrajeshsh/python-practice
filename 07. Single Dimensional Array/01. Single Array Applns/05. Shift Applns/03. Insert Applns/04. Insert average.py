import os 
os.system("cls")

print("Insert average between each pair of elements of array:")
n = int(input("Enter number of elements: "))
print()

nums= []
for i in range(n):
    print("Enter element #",i+1,": ",sep='', end='')
    nums.append(int(input()))

print("\nThe original array:\n",nums,"\n", sep='')

i = 1
while i < len(nums):
    nums.insert(i,(nums[i]+nums[i-1])/2)
    i+=3

print("\nArray elements after inserting the average between every pair of elements:\n",
            nums,"\n", sep='')