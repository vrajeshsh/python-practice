import os
os.system("cls")

def sortorder(arr):
    global asc_cnt, desc_cnt
    if len(arr)==1:
        return ""
    if arr[0]<=arr[1]:
        asc_cnt+=1
    if arr[0]>=arr[1]:
        desc_cnt+=1
    sortorder(arr[1:])
    return 1 if asc_cnt==len(arr)-1 else 2 if desc_cnt==len(arr)-1 else 3

print("To determine the order in which the array is sorted: ")
n = int(input("Enter number of elements: "))

arr, asc_cnt, desc_cnt = [], 0, 0
for i in range(1, n+1):
    print("Enter element #",i,": ", sep='', end='')
    arr.append(int(input()))

order= sortorder(arr)

print("\nThe array:\n",arr,sep='')
print("\nThe array elements are sorted in ", 
    ("ascending" if order==1 else "descending" if order==2 else "no specific"), " order.\n", sep='')