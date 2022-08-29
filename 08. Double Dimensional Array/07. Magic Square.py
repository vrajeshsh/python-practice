import os
os.system("cls")

print("To check if the given 2-D matrix is a Magic Square having the sums of each rows/colums/diagonals equal:")
n = int(input("Enter number of rows/columns for the square matrix: "))
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

diag1_sum, diag2_sum, isMagic = 0, 0, True
for i in range(n):
    row_sum, col_sum = 0, 0
    diag1_sum+= num[i][i]  
    diag2_sum+= num[i][n-i-1]
    for j in range(n):
        row_sum+=num[i][j]
        col_sum+=num[j][i]
    if row_sum != col_sum:
        isMagic = False

if col_sum==diag1_sum==diag2_sum and isMagic:
    print("\nThe square matrix is a Magic square!\n")
else:
    print("\nThe square matrix is NOT a Magic square!\n")