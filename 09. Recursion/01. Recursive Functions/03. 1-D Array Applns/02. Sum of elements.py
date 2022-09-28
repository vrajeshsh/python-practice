import os
os.system("cls")

def sumofelements(arr):
    # w/ slicing
    # if len(arr)==1:
    #     return arr[0]
    # return arr[0]+sumofelements(arr[1:]) # Try WITHOUT 'slicing' for a Welcome Change

    #w/o slicing
    if len(arr)==0:
        return 0
    return arr.pop()+sumofelements(arr) # Do you think pop() exists in other languages? 

'''
Consider that 'slicing' is unique to Python. Does that mean the recursion would not work in other
languages where there is NO SLICING?
Try to develop the code in a GENERIALIZED way... so that it works universally in all languages!!!
Good to see that you picked up slicing so well and found out an uncanny way to use it in recursion.
'''

print("To find the sum of all elements of an array:")
n = int(input("Enter number of elements: "))

arr = []
for i in range(1, n+1):
    print("Enter element #",i,": ", sep='', end='')
    arr.append(int(input()))

print("\nThe array:\n",arr,sep='')
print("\nSum of all elements of the array are: ",sumofelements(arr),"\n", sep='')
