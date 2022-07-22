import os
os.system("cls")

print("To display the frequency of each element in array:")
n = int(input("Enter number of elements: "))
print()

nums,count= [], 0

for i in range(n):
    print("Enter element #", i+1,": ", sep='', end='')
    nums.append(int(input()))

lgt = len(nums)
print("\nELEMENT\t\tFREQUENCY")
for i in range(lgt):
    if nums[i] not in nums[:i]:
        print(nums[i],"\t\t",nums.count(nums[i]))
print()
