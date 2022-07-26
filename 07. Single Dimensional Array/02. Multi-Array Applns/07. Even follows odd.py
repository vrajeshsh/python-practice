import os
os.system("cls")

print("To print all odd elements followed by even ones of two arrays")
n1 = int(input("Enter number of elements in first array: "))
n2 = int(input("Enter number of elements in second array: "))

nums1, nums2, nums3, j = [], [], [], 0

print("\nEnter the", n1,"elements for the first array below:")
for i in range(n1):
    print("Enter element #",i+1,": ",sep='', end='')
    nums1.append(int(input()))
    
print("\nEnter the", n2,"elements for the second array below:")
for i in range(n2):
    print("Enter element #",i+1,": ",sep='', end='')
    nums2.append(int(input()))

for i in nums1+nums2:
    if i%2:
        nums3.insert(j,i)
        j+=1
    else:
        nums3.append(i)

print("\nFirst array:\n", nums1,
    "\n\nSecond array:\n", nums2,
    "\n\nNew array:\n", nums3, "\n",sep='')
