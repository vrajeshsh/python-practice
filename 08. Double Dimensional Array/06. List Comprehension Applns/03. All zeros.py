import os
os.system("cls")

print("To find rows, columns, diagonal which has all elements as zeros:")
n = int(input("Enter number of rows/columns for square matrix: "))
print()

num = [[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        print("Enter element at position ("+str(i+1),", "+str(j+1)+"): ", end='', sep='')
        num[i][j] = int(input())

print("\nThe elements of the 2-D array:")
for i in range(n):
    for j in range(n):
        print(num[i][j],"\t",sep='', end='')
    print()

leftdiag, rightdiag = [num[i][i] for i in range(n)], [num[i][n-1-i] for i in range(n)]
for i in range(n):
    row, col = num[i], [col[i] for col in num]
    if row.count(0)==len(row):
        print("Row #",i+1," has all zeros!", sep='')
    elif col.count(0)==len(col):
        print("Column #",i+1," has all zeros!", sep='')

if leftdiag.count(0)==len(leftdiag):
    print("Left Diagonal has all zeros!")
elif rightdiag.count(0)==len(rightdiag):
    print("Right Diagonal has all zeros!")
print()
