import os
os.system("cls")

def sortorder(array): # to check if the input arrays are in right order
    

def getmergedsorted(asc, desc):


asc, desc = [], []

print("To merge Ascending and descending arrays into a single ascending array:")
n1 = int(input("Enter number of elements in the first array: "))
n2 = int(input("Enter number of elements in the second array: "))
print("\nEnter", n1,"elements in ASCENDING ORDER below:")
for i in range(n1):
    print("Enter element #",i+1,": ",sep='', end='')
    asc.append(int(input()))
print("\nEnter", n2,"elements in DESCENDING ORDER below:")
for i in range(n2):
    print("Enter element #",i+1,": ",sep='', end='')
    desc.append(int(input()))

if sortorder(asc) != 1:
    print("\nFirst array elements are NOT in ascending order!")
elif sortorder(desc) != 2:
    print("\nSecond array elements are NOT in descending order!")
else:
    mergesorted = getmergedsorted(asc, desc)
    print("\nFirst array elements (in ascending order):\n", asc,
        "\n\nSecond array elements (in descending order):\n", desc,
        "\n\nMerge and sorted array elements (in ascending order):\n", 
            mergesorted, sep='')
