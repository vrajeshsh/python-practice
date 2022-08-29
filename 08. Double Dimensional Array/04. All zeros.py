import os
os.system("cls")

print("To find rows, columns or diagonals which have all zeros:")
n = int(input("Enter number of rows/columns for square matrix: "))
print()

num, isRowPresent, isColPresent = [], False, False
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
l_diag, r_diag =  0, 0
for i in range(n):
    row_cnt, col_cnt = 0, 0
    if num[i][i]==0:
        l_diag+=1
    if num[i][n-i-1]==0:
        r_diag+=1
    for j in range(n):
        if num[i][j]==0:
            row_cnt+=1
        if num[j][i]==0:
            col_cnt+=1
    if row_cnt==n:
        isRowPresent = True
        print("Row #",i+1," has all zeros!", sep='')
    if col_cnt==n:
        isColPresent = True
        print("Column #",i+1," has all zeros!", sep='')

if l_diag==n:
    print("Left Diagonal has all zeros!", sep='')
if r_diag==n:
    print("Right Diagonal has all zeros!", sep='')
elif not(l_diag==n or r_diag==n or isRowPresent or isColPresent):
    print("\nNo row, column or diagonal has all zeros in the matrix!")
print()