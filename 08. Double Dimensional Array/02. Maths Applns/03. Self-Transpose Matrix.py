import os
os.system("cls")

def displayMatrix(num):
    for i in range(n):
        for j in range(n):
            print(num[i][j],"\t",end="")
        print()

print("To self transpose a given square matrix: ")
n = int(input("Enter the number of rows/columns: "))
print()

num = [[0]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        print("Enter integer for element at (",
            str(i+1)+", "+str(j+1)+"): ", end= "", sep= "")
        num[i][j] = int(input())
        
print("\nThe elements of the 2-D array: ")
displayMatrix(num)

for i in range(n):
    for j in range(i+1, n):
        num[i][j], num[j][i] = num[j][i], num[i][j]

print("\nThe given matrix after self-transposing: ")
displayMatrix(num)
print()