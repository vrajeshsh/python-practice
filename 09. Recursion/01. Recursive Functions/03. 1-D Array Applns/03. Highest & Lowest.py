import os
os.system("cls")

def maxelement(arr):
    if len(arr)==1:
        return arr[0]
    maxi = maxelement(arr[1:])
    return maxi if maxi>arr[0] else arr[0]

def minelement(arr):
    if len(arr)==1:
        return arr[0]
    mini = minelement(arr[1:])
    return mini if mini<arr[0] else arr[0]

print("To find the maximum and minimum of an array:")
n = int(input("Enter number of elements: "))
arr = []
for i in range(1, n+1):
    print("Enter element #",i,": ", sep='', end='')
    arr.append(int(input()))

print("\nThe array:\n",arr,sep='')

print("\nThe highest element: ", maxelement(arr),
    "\nThe lowest element: ", minelement(arr),"\n", sep='')
