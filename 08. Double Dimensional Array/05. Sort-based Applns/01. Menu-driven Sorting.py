from http.client import CannotSendHeader
import os
os.system("cls")

def displayMatrix(num):
    for i in range(n):
        for j in range(n):
            print(num[i][j],"\t",end="")
        print()

def sortRows(num):
    for i in range(n):
        num[i].sort()
        
def sortColumns(num): 
    for i in range(n):
        for j in range(n):
            for k in range(n-i-1):
                if num[k][j] > num[k+1][j]:
                    num[k][j], num[k+1][j] = num[k+1][j], num[k][j]

def sortDiagonals(num):
    for i in range(n):
        for j in range(n):
            if num[i][i]<num[j][j]:
                num[i][i], num[j][j] = num[j][j], num[i][i]
            if num[i][n-i-1]<num[j][n-j-1]:
                num[i][n-i-1], num[j][n-j-1] = num[j][n-j-1], num[i][n-i-1]
        
n = int(input("Enter number of rows/columns: "))
print()

num = [[0]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        print("Enter integer for element at (",
            str(i+1)+", "+str(j+1)+"): ", end= "", sep= "")
        num[i][j] = int(input())   

ch = 0
while ch!=4:
    print("\nSorting in 2-D array:",
    "\n1. Sort the rows",
    "\n2. Sort the columns",
    "\n3. Sort the Diagonals",
    "\n4. Exit Program")
    ch = int(input("Enter your choice [1 - 4]: "))
    print("\nThe elements of the 2-D array as given:")
    displayMatrix(num)
    if ch==1:
        sortRows(num)
        print("\nThe elements of the 2-D array after sorting the Rows:")
        displayMatrix(num)
    elif ch==2:
        sortColumns(num)
        print("\nThe elements of the 2-D array after sorting the Columns:")
        displayMatrix(num)
    elif ch==3:
        sortDiagonals(num)
        print("\nThe elements of the 2-D array after sorting the Diagonals:")
        displayMatrix(num)
    elif ch==4:
        print("\nThank You!\n")
    else:
        print("\nIncorrect choice! Select choice between 1 - 4!\n")

'''
Make the following changes in this program:
1. Present the given matrix always before each sorted matrix.
2. Check the Right-diagonal sorting code. Its not working. And in my opinion you Cannot  
use the or operator that way to sort both the diagonals.. Its usually done one after another  but
frugally....
'''