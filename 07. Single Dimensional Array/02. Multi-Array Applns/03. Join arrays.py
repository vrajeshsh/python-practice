import os
os.system("cls")

nums1, nums2 = [], []

print("To join two arrays: ")
n1 = int(input("Enter number of elements in first array: "))
n2 = int(input("Enter number of elements in second array: "))

print("\nEnter the", n1,"elements for the first array below:")
for i in range(n1):
    print("Enter element #",i+1,": ",sep='', end='')
    nums1.append(int(input()))
print("\nEnter the", n2,"elements for the second array below:")
for i in range(n2):
    print("Enter element #",i+1,": ",sep='', end='')
    nums2.append(int(input()))

print("\nFirst array elemennts:\n",nums1,
    "\n\nSecond array elemennts:\n",nums2, sep='')

nums1+= nums2

print("\nThe first array after join:\n", nums1,"\n", sep='')
