import os
os.system("cls")

print("To display the duplicates present in the array:")
n = int(input("Enter the number of elements: "))
print()

nums,dups = [], ""
for i in range(n):
    print("Enter the element #",i+1,": ",sep='',end='')
    nums.append(int(input()))
    if nums[i] in nums[:i] and str(nums[i]) not in dups:
        dups+= str(nums[i]) if dups=='' else ", "+str(nums[i])

print("\nThe array:\n",nums)
if dups!="":
    print("\nThe duplicate elements present in the array:\n",dups,"\n",sep='')
else:
    print("\nNo duplicate element found in the array!\n")