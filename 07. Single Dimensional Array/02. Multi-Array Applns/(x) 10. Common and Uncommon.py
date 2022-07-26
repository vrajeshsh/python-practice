import os
os.system("cls")

nums1, nums2, nums3, common, uncommon = [], [], [], [], []

print("To find the common and uncommon elements of two arrays:")
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

nums3=nums1+nums2
count = 0
for i in range(len(nums3)):
    count = nums3.count(nums3[i])
    if count>1 and nums3[i] not in common:
        for j in range(count):
            common.append(nums3[i])
    elif count==1:
        uncommon.append(nums3[i])

print("\nThe first array:\n",nums1,
        "\n\nThe second array:\n",nums2,
        "\n\nCommon elements:\n",common,
        "\n\nUncommon elements:\n",uncommon,"\n", sep='')

''' Fix the code after considering the faulty I/O given below:
The first array:
[12, 23, 34, 45, 67, 34]

The second array:
[12, 23, 12, 45, 78, 89, 78, 56]

Common elements:
[12, 12, 12, 23, 23, 34, 34, 45, 45, 78, 78]
(78 repeats TRUE. But it's not a common element)

Uncommon elements:
[67, 89, 56]
(Multiple copies of the uncommon elements are not getting stored)
'''