import os
os.system("cls")

n = int(input("Enter number of rows/columns for the square matrix: "))
print()
num = []
for i in range(n):
    _ = []
    for j in range(n):
        elem = int(input("Enter for row #"+str(i+1)+" and column #"+str(j+1)+": "))
        _.append(elem)
    num.append(_)

print("\nThe elements of the 2-D array:")
for i in range(n):
    for j in range(n):
        print(num[i][j],"\t",end='')
    print()
print()

diag1_sum, diag2_sum, ssum = 0, 0, 0
for i in range(n):
    row_sum, col_sum = 0, 0
    diag1_sum+= num[i][i]  
    diag2_sum+= num[i][n-i-1]
    for j in range(n):
        row_sum+=num[i][j]
        col_sum+=num[j][i]
        ssum+=num[i][j]
    print("Sum of row #",i+1,": ",row_sum, sep='')
    print("Sum of column #",i+1,": ",col_sum,"\n", sep='')

print("\nSum of the first diagonal: ", diag1_sum,
    "\nSum of the second diagonal: ", diag2_sum,
    "\n\nSum of all the elements: ", ssum,"\n",sep='')
