import os
os.system("cls")

nums1, nums2, union, intersection = [], [], [], []

print("To find the intersection and union of two arrays:")
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
    
for i in range(n1):
    if nums1[i] in nums2 and nums1[i] not in intersection:
        intersection.append(nums1[i])
for elem in (nums1+nums2):
    if elem not in union:
        union.append(elem)

print("\nThe first array:\n",nums1,"\n\nThe second array:\n",nums2,
        "\n\nIntersection set elements:\n",intersection,
        "\n\nUnion set elements:\n",union,"\n", sep='')