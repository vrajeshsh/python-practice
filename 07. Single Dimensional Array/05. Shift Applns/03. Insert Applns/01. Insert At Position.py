import os
os.system("cls")

print("To insert element at specified position in array:")
n = int(input("Enter number of elements: "))
print()

nums = []
for i in range(n):
    print("Enter element #",i+1,": ",sep='', end='')
    nums.append(int(input()))

print("\nThe original array:\n",nums,"\n", sep='')
new_ele = int(input("Enter element to insert: "))
pos = int(input("Enter position of insertion: "))

if 1 <= pos <= n:
    nums.insert(pos-1, new_ele)
    print("\nArray elements after inserting ",new_ele," at position ",pos,":\n",nums,"\n", sep='')
else:
    print("\nInvalid position entered! Enter a position between 1 and ",n," only!\n", sep='')
