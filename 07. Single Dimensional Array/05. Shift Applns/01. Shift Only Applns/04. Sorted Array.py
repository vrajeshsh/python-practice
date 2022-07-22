import os
os.system("cls")

print("Accept numbers in a sorted manner:")
n = int(input("Enter number of elements: "))
print()

nums, i = [], 0
while i<n:
    print("Enter element #",i+1,": ",sep='', end='')
    temp = int(input())
    if nums==[] or temp>=nums[i-1]:
        nums.append(temp)
        i+=1
    else:
        print("Please enter a number greater than",nums[i-1])

print("\nArray as given:\n",nums,sep='')

ins = int(input("\nEnter number to insert: "))

for i in range(n):
    if nums[i]>ins:
        nums.insert(i, ins)
        break

print("\nArray after insertion:\n",nums,"\n",sep='')