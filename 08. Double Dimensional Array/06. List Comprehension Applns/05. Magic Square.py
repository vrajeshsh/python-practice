import os
os.system("cls")

def isMagicSquare(num):
    l_diag_sum = sum([num[i][i] for i in range(n)])
    r_diag_sum = sum([num[i][n-i-1] for i in range(n)])

    if l_diag_sum!=r_diag_sum:
        return False
    for i in range(n):
        row_sum=sum(num[i])
        col_sum=sum([col[i] for col in num])
        if row_sum!=l_diag_sum or col_sum!=l_diag_sum:
            return False
    return True
    
print("To check if a given 2-D array forms a Magic Square")
n = int(input("Enter number of rows/columns for the square matrix: "))
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

if isMagicSquare(num):
    print("\nThe given square matrix is a Magic Square!\n")
else:
    print("\nThe given square matrix is NOT a Magic Square!\n")
