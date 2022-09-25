import os
os.system("cls")

def displayMatrix(num):
    for i in range(n):
        for j in range(n):
            print(num[i][j],"\t",end="")
        print()

def sortRows(num):
    new2D = [row[:] for row in num]
    for i in range(n):
        new2D[i] = sorted(num[i])
    return new2D

def sortColumns(num): 
    new2D, r, c = [row[:] for row in num], len(num), len(num[0])
    for i in range(c):
        col = sorted([col[i] for col in new2D])
        for j in range(r):
            new2D[j][i] = col[j]
    return new2D

def sortDiagonals(num):
    new2D = [row[:] for row in num]
    l_diag = sorted([num[i][i] for i in range(n)])
    r_diag = sorted([num[i][n-i-1] for i in range(n)])
    for i in range(n):
        new2D[i][i] = l_diag[i]
        new2D[i][n-1-i] = r_diag[i]
    return new2D
        
n = int(input("Enter number of rows/columns for the square matrix: "))
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
        print("\nThe elements of the 2-D array after sorting the Rows:")
        displayMatrix(sortRows(num))
    elif ch==2:
        print("\nThe elements of the 2-D array after sorting the Columns:")
        displayMatrix(sortColumns(num))
    elif ch==3:
        print("\nThe elements of the 2-D array after sorting the Diagonals:")
        displayMatrix(sortDiagonals(num))
    elif ch==4:
        print("\nThank You!\n")
    else:
        print("\nIncorrect choice! Select choice between 1 - 4!")
