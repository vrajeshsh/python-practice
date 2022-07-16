from email.errors import InvalidBase64CharactersDefect
import os
from platform import python_branch

from pkg_resources import to_filename
os.system("cls")

print("To shift all zeros to front of array:")
n = int(input("Enter the number of elements: "))
print()

nums, start = [], 0

for i in range(n):
    print("Enter element #",i+1,": ",sep='', end='')
    nums.append(int(input()))

print("\nThe original array:\n", nums, sep = '')

for i in range(n):
    if nums[i]==0:
        nums.insert(start, nums.pop(i))
        start+= 1

print("\n\nThe array after shifting zeros to the front:\n",nums, "\n", sep='')

# pop() happens first. As soon as an element is popped, the size contracts...to  
# adjust for the removal.  Now when you insert the popped element it gets inserted at a new location (start+1)
# and again the size gets increased to accomodate the new element.n
# This way the duo work...
