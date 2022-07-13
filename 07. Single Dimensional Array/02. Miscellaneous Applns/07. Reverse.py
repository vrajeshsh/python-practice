import os
os.system("cls")

def reverse_list(num):
    n = len(num)
    for i in range(n//2):
        temp = num[i]
        num[i] = num[n-i-1]
        num[n-i-1] = temp

nums = []
print("To reverse the elements of an array")
n = int(input("Enter number of elements: "))
print()

for i in range(n):
    print("Enter element #", i+1,": ", sep='', end='')
    nums.append(int(input()))

print("\nThe Original array:\n",nums, sep='')

reverse_list(nums)

print("\nIt's reverse:\n", nums,"\n", sep='')
