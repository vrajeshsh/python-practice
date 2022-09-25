import os
os.system("cls")

def displayMatrix(num):
    for i in range(n):
        for j in range(n):
            print(num[i][j],"\t",end="")
        print()

def sortDiagonal(num, ch, n, order):
# Use 2 small conditional expn to shorten the code... this requires only OBSERVATION!!
    for i in range(n-1):
        for j in range(i+1, n):
            if num[i][i]>num[j][j] or num[i][n-i-1]>num[j][n-j-1]:
                num[i][i], num[j][j], num[i][n-i-1], num[j][n-j-1] = num[j][j], num[i][i], num[j][n-j-1], num[i][n-i-1]
            

print("To sort either of the diagonals in Ascending or Descending: ")
n = int(input("Enter the number of rows / columns: "))
print()

num = [[0]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        print("Enter integer for element at (",
            str(i+1)+", "+str(j+1)+"): ", end= "", sep= "")
        num[i][j] = int(input())    

print("\nThe elements of the 2-D square matrix: ")
displayMatrix(num)

ch = int(input("\nChoice of diagonal [1. Left 2. Right]: "))
order = int(input("Choice of order [1. Ascending 2. Descending]: "))

sortDiagonal(num, ch, n, order)

ch = "Left" if ch==1 else "Right"
order = "Ascending" if order == 1 else "Descending"

print("\nThe 2-D array after sorting",ch,"diagonal in",order,"order:")
displayMatrix(num)
print()