import os
from xmlrpc.client import Marshaller
os.system("cls")

print("To shift all negative elements to the end:")
n = int(input("Enter the number of elements: "))
print()

nums, start = [], 0

for i in range(n):
    print("Enter element #",i+1,": ",sep='', end='')
    nums.append(int(input()))

print("\nThe original array:\n", nums, sep = '')

for i in range(n):
    if nums[i]>=0:
        nums.insert(start, nums.pop(i))
        start+= 1

print("\nThe array after negative elements to the end:\n",nums, "\n", sep='')

# but sir you asked to insert at end right
# i simply moved the positive to front.....

# This I call '(Rishi) Valmiki' style.  Probably you WERE that Great person in  
# one of your previous lives...

# He would not say Ram at all... So the Great Naradmuni advised him to say Mra  
# which if pronounced fast sounds Ram only...

# Valid. But a little awkward... ok sir got it..