import os
from xml.dom.expatbuilder import theDOMImplementation
os.system("cls")

nums1, nums2, nums3 = [], [], []

print("To merge two arrays into an array and sort it: ") 
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

nums3 = sorted(nums1+nums2) 

print("\nThe first array:\n", nums1,"\n\nThe second array:\n",nums2,sep='')
print("\nMerged array:\n",nums3,"\n", sep='')
