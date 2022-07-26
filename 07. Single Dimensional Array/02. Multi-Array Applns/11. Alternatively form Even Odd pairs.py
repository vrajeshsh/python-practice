import os
os.system("cls")

nums1, nums2, nums3, ecnt, ocnt, indx1, indx2 = [], [], [], 0, 0, 0, 1

print("To pair even and odd elements of an array:")
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

for elem in nums1+nums2:
    if elem%2==0:
        ecnt+= 1
        nums3.insert(indx1, elem)
        indx1+= 2
    else:
        ocnt+= 1
        nums3.insert(indx2, elem)
        indx2+= 2
del nums3[min(ecnt, ocnt)*2:]

print("\nFirst array elements:\n", nums1,
    "\n\nSecond array elements:\n", nums2,
    "\n\nAlternatively merged even-odd elements:\n", nums3, sep='')
