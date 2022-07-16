import os
os.system("cls")

print("To segragate all even and odd elements in an array:")
n = int(input("Enter the number of elements: "))
print()

nums, start, end = [], 0, n
for i in range(n):
    print("Enter element #",i+1,": ",sep='', end='')
    nums.append(int(input()))

print("\nThe original array:\n", nums, sep = '')

for i in range(n):
    if nums[i]%2:
        nums.insert(start, nums.pop(i))
        start+= 1
    elif nums[i]==0:
        nums.insert(start, nums.pop(i))
    
print("\nAfter shifting even elements to the start and odd to the end:\n",nums, "\n", sep='')
