import os
os.system("cls")

# Design the below function to swap the front and back elements continuously to 
# physically reverse the elements

# without any more parameters? Obviously!! You are already aware with such techniques!!
def reverse(arr):
    if len(arr)<=1:
        return arr
    arr[0], arr[-1] = arr[-1], arr[0]
    
    reverse(arr[1:-1]) 

print("To reverse the elements of an array: ")
n = int(input("Enter number of elements: "))

arr = []
for i in range(1, n+1):
    print("Enter element #",i,": ", sep='', end='')
    arr.append(int(input()))

print("\nThe array:\n",arr,sep='')
reverse(arr)
print("\nReverse of the array:\n",arr,"\n",sep='')

