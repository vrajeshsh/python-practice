import os
os.system("cls")

def displayMatrix(num):
    for i in range(n):
        for j in range(n):
            print(num[i][j],"\t",end="")
        print()

print("To swap the elements of the left and right diagonals: ")
n = int(input("Enter number of rows / columns: "))
print()

num = [[0]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        print("Enter integer for element at (",
            str(i+1)+", "+str(j+1)+"): ", end= "", sep= "")
        num[i][j] = int(input())    

print("\nThe elements of the 2-D square matrix: ")
displayMatrix(num)

for i in range(n):
    num[i][i], num[i][n-i-1] = num[i][n-i-1], num[i][i]

print("\nAfter swapping the diagonals: ")
displayMatrix(num)
print()