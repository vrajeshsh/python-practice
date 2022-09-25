import os
os.system("cls")

def displayMatrix(num):
    for i in range(n):
        for j in range(n):
            print(num[i][j],"\t",end="")
        print()

def sortNonBoundaryElements(num, r, c):
    rearranged = sorted([num[i][j] for i in range(r) for j in range(c) if i!=0 and i!=r-1 and j!=0 and j!=c-1])
    new2D =  [row[:] for row in num]
    k=0
    for i in range(r):
        for j in range(c):
            if i!=0 and i!=r-1 and j!=0 and j!=c-1:
                new2D[i][j]=rearranged[k]
                k+=1
    return new2D

def getDiagonalSum(num, n):
    l_diag, r_diag = [num[i][i] for i in range(n)], [num[i][n-1-i] for i in range(n)]
    return sum(l_diag)+sum(r_diag)

def getDiagonalElements(num, n):
    for i in range(n):
        for j in range(n):
            if i==j or i==n-j-1:
                print(num[i][j],"\t", end='')
            else:
                print("\t", end='')
        print()

print("To sort the non-boundary elements of a matrix and calculate the sum of diagonals:")
n = int(input("Enter number of rows/columns: "))
print()

num = [[0]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        print("Enter integer for element at (",
            str(i+1)+", "+str(j+1)+"): ", end= "", sep= "")
        num[i][j] = int(input())

print("\nThe elements of the 2-D array as given:")
displayMatrix(num)
print("\nThe diagonal elements:")
print(getDiagonalElements(num, n))
print("\nThe non-boundary elements of the rearraged 2-D array:")
displayMatrix(sortNonBoundaryElements(num, n, n))
print("\n\nSum of diagonal elements =",getDiagonalSum(num, n),"\n")
