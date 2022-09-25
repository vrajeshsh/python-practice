import os
os.system("cls")

def isSymmetric(num):
    for i in range(n):
        for j in range(n):
            if num[i][j] != num[j][i]:
                return False
    return True

print("To check whether the given matrix is Symmetric or not: ")
n = int(input("Enter the number of rows/columns: "))
print()

num = [[0]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        print("Enter integer for element at (",
            str(i+1)+", "+str(j+1)+"): ", end= "", sep= "")
        num[i][j] = int(input())

print("\nThe elements of the 2-D array: ")
for i in range(n):
    for j in range(n):
        print(num[i][j],"\t",end="")
    print()

if isSymmetric(num):
    print("\nThe given 2-D array is a Symmetric Matrix!\n")
else:
    print("\nThe given 2-D array is NOT a Symmetric Matrix!\n")
