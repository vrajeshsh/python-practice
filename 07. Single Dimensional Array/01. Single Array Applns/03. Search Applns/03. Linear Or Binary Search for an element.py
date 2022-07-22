import os
os.system("cls")

def sortorder(nums):
    lgt, asc_cnt, desc_cnt = len(nums), 1, 1
    for i in range(lgt-1):
        if nums[i]<=nums[i+1]:
            asc_cnt+=1
        if nums[i]>=nums[i+1]:
            desc_cnt+=1
    return 1 if asc_cnt==n else 2 if desc_cnt==n else 0

def linearSearch(nums, x):
    lgt = len(nums)
    for i in range(lgt):
        if nums[i] == x:
            return i+1

def binarySearch(nums, x):
    order, low, high = sortorder(nums), 0, len(nums)-1
    while low < high:
        mid = (low + high)//2
        if nums[mid] == x:
            return mid+1
        elif nums[mid] < x if order==1 else nums[mid] > x:
            low = mid+1
        else:
            high= mid-1
    return -1

print("To search an element using Binary or Linear search:")
n = int(input("Enter the number of elements: "))
print()

nums = []
for i in range(n):
    print("Enter the element #",i+1,": ",sep='',end='')
    nums.append(int(input()))

x, order = int(input("Search for: ")), sortorder(nums)

if order:
    pos= binarySearch(nums, x)    
    print("\nThe array is found sorted in","ascending" if order==1 else "descending","order!",
        "\nHence Binary Search technique has been adopted for search.")
else:
    pos= linearSearch(nums, x)
    print("\nThe array is found not sorted!",
        "\nHence Linear Search technique has been adopted for search.")
if pos:        
    print("The element ",x," occurs at position ",pos,".\n", sep='')
else:
    print("The element ",x," was not found in the array!", sep='')    
