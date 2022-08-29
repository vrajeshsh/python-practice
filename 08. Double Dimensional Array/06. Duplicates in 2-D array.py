import os
os.system("cls")

print("To find rows, columns or diagonals which have duplicate elements:")
n = int(input("Enter number of rows/columns for square matrix: "))
print()

num = []
for i in range(n):
    _ = []
    for j in range(n):
        elem = int(input("Enter element for row #"+str(i+1)+" and column #"+str(j+1)+": "))
        _.append(elem)
    num.append(_)

print("\nThe elements of the 2-D array:")
for i in range(n):
    for j in range(n):
        print(num[i][j],"\t", end='')
    print()
print()

l_diag, r_diag, l_diag_dups, r_diag_dups =  [], [], [], []
for i in range(n):
    row, row_dups= [], []
    col, col_dups= [], []
    if num[i][i] in l_diag and num[i][i] not in l_diag_dups:
        l_diag_dups.append(num[i][i])
    else:
        l_diag.append(num[i][i])
    if num[i][n-i-1] in r_diag and num[i][n-i-1] not in r_diag_dups:
        r_diag_dups.append(num[i][n-i-1])
    else:
        r_diag.append(num[i][n-i-1])
    for j in range(n):
        if num[i][j] in row and num[i][j] not in row_dups:
            row_dups.append(num[i][j])
        else:
            row.append(num[i][j])
        if num[j][i] in col  and num[j][i] not in col_dups:
            col_dups.append(num[j][i])
        else:
            col.append(num[j][i])
    if row_dups:
        print("Row #",i+1," has ",row_dups," as duplicate element(s)!", sep='')
    if col_dups:
        print("Column #",i+1," has ",col_dups," as duplicate element(s)!", sep='')
    
if l_diag_dups:
    print("Left Diagonal has ",l_diag_dups,"as the duplicate element(s)", sep='')
if r_diag_dups:
    print("Right Diagonal has ",r_diag_dups,"as the duplicate element(s)", sep='')
elif not(l_diag_dups or r_diag_dups or row_dups or col_dups):
    print("\nNo row, column or diagonal has any duplicates in the matrix!")
print()
