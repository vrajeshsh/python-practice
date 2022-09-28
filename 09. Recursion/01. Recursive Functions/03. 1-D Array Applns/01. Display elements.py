import os
os.system("cls")
# True, you got real success while tackling the string based recursion problems.
# But that does not mean that you would go on applying/converting ALL CONCEPTS
# down to string only!!!

def showelements(arr):
    if len(arr)==0:
        print()
        return ""
    print(arr[0],", ", sep='', end='')
    return showelements(arr[1:])
    
arr= []
print("To display the elements of an array: ")
n = int(input("Enter number of elements: "))
for i in range(n):
    print("Enter element #",i+1,": ", sep='', end='')
    arr.append(int(input()))

print("\nThe elements of the array are:")
showelements(arr)
print()