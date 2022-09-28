import os
os.system("cls")

def occurences(srchelem, arr):
    if len(arr)==0:
        return 0
    if arr[0]==srchelem:
        return 1+occurences(srchelem, arr[1:])
    return occurences(srchelem, arr[1:])

print("To find the number of occurances of a particular element in an array:")
n = int(input("Enter number of elements: "))

arr = []
for i in range(1, n+1):
    print("Enter element #",i,": ", sep='', end='')
    arr.append(int(input()))

srchelem = int(input("\nEnter the element to be searched: "))

print("\nThe array:\n",arr,sep='')
count = occurences(srchelem, arr)

if count>0:
    print("\n", srchelem," occurs in the array ", count," time(s)!\n", sep='')
else:
    print("\n",srchelem," is NOT present in the array!\n", sep='')