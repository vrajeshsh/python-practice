import os
from ssl import PEM_cert_to_DER_cert
os.system("cls")

print("Display first half of array in Ascending order and secodn half in Descending order:")
n = int(input("Enter number of elements: "))
print()

nums = []
for i in range(n):
    print("Enter element #",i+1,": ",sep='', end='')
    nums.append(int(input()))

print("\nThe array:\n",nums,sep='')

nums = sorted(nums[0:n//2])+sorted(nums[n//2:n], reverse = True)

print("\nArray after sorting fist half in Ascending and second half in descending order:\n",
        nums,"\n",sep='')
