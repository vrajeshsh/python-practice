import os
os.system("cls")

def ispresent(srchelem, arr):
    if len(arr)==0:
        return False

    # W/ slicing
    # if arr[0]==srchelem:
    #     return True
    # return ispresent(srchelem, arr[1:])

    # W/O slicing
    if arr[len(arr)-1]==srchelem:
        return True
    arr.pop()
    return ispresent(srchelem, arr)

arr = []

print("To find an element in an array:")
n = int(input("Enter number of elements: "))

for i in range(1, n+1):
    print("Enter element #",i,": ", sep='', end='')
    arr.append(int(input()))

srchelem = int(input("\nEnter the element to be searched: "))

print("\nThe array:\n",arr,sep='')

print("\nThe element ",srchelem," is ","" if ispresent(srchelem, arr) else "NOT ","present in the array!\n", sep='')