import os
os.system("cls")

def isEqual(num):
    l_diag=[num[i][i] for i in range(n)]
    r_diag=[num[i][n-i-1] for i in range(n)]

    return True if l_diag==r_diag else False

def isSimilar(num):
    l_diag=[num[i][i] for i in range(n)]
    r_diag=[num[i][n-i-1] for i in range(n)]

    return True if sorted(l_diag)==sorted(r_diag) else False

print("To check if diagonals of a square matrix are Equal and Similar: ")
n = int(input("Enter number of rows/columns of the square matrix: "))
print()

num = [[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        print("Enter element for position (",i+1,", ",j+1,"): ", sep='', end='')
        num[i][j] = int(input())

print("\nThe elements of the 2-D array:")
for i in range(n):
    for j in range(n):
        print(num[i][j],"\t",end='')
    print()

if isEqual(num):
    print("\nThe diagonals of the given array are equal and similar!\n")
elif isSimilar(num):
    print("\nThe diagonals of the given array are similar!\n")
else:
    print("\nThe diagonals of the given array are neither equal nor similar!\n")