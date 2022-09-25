import os
os.system("cls")

print("To find rows, columns or diagonals that have duplicate elements in them")
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
print()

# Kindly use strings to store the duplicates and NOT lists for presentation purposes without
# compromising the code length.

l_diag_dups, r_diag_dups = "", ""

l_diag=[num[i][i] for i in range(n)]
r_diag=[num[i][n-i-1] for i in range(n)]

l_diag_dups+=[str(i) for i in l_diag if l_diag.count(i)>1 and i not in l_diag_dups]
r_diag_dups+=[str(i) for i in r_diag if r_diag.count(i)>1 and i not in r_diag_dups]
for i in range(n):
    row_dups, col_dups = [], []
    row, col = num[i], [col[i] for col in num]
    row_dups+=[str(j) for j in row if row.count(j)>1 and j not in row_dups]
    col_dups+=[str(j) for j in col if col.count(j)>1 and j not in col_dups]
    if row_dups:
        print("Row #",i+1," has ",row_dups," as duplicate element(s)!", sep='')
    if col_dups:
        print("Column #",i+1," has ",col_dups," as duplicate element(s)!", sep='')

if l_diag_dups:
    print("Left Diagonal has ",l_diag_dups," as duplicate element(s)!", sep='')
if r_diag_dups:
    print("Right Diagonal has ",r_diag_dups," as duplicate element(s)!", sep='')
if not (l_diag_dups or r_diag_dups or row_dups or col_dups):
    print("No row, column, or diagonal has any duplicates in the matrix!")
print()

#Keep these two programs SOLVED/FIXED for tomorrow's class...