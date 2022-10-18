import os
os.system("cls")
'''
Below function is NOT WORKING. Fix it whenever free.
The array:
[98, 87, 76, 76, 54, 43, 21, 12, 2]

 21  is NOT present in the array!
'''
def binarysearch(arr, srchelem, p1, p2):
    if p2>=p1:
        mid = (p1+p2)//2
        if arr[mid]==srchelem:
            return mid
        elif arr[mid]>srchelem:
            return binarysearch(arr, srchelem,p1,mid-1)
        else:
            return binarysearch(arr, srchelem,mid+1,p2)
    else:
        return -1

print("To search for an element in array using binary search:")
n = int(input("Enter number of elements: "))

arr = []
for i in range(1, n+1):
    print("Enter element #",i,": ", sep='', end='')
    arr.append(int(input()))

srchelem = int(input("\nEnter the element to search: "))

print("\nThe array:\n",arr,sep='')

srchpos = binarysearch(arr, srchelem, 0, n)+1
if srchpos==-1:
    print("\n",srchelem," is NOT present in the array!\n")
else:
    print("\n",srchelem," is present at position: ", srchpos,"\n", sep='')
