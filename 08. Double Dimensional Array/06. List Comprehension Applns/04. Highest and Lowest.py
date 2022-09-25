import os
os.system("cls")

print("To print the highest and lowest elements of each row/column:")
r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))
print()

num = [[0]*c for i in range(r)]
for i in range(r):
    for j in range(c):
        print("Enter element at position (",i+1,", ",j+1,"): ", sep='', end = '')
        num[i][j] = int(input())

print("\nThe elements of the 2-D matrix are as follows: ")
for i in range(r):
    for j in range(c):
        print(num[i][j],"\t", sep='', end = '')
    print()

for i in range(r):
    row_max = max(num[i])
    row_max_pos = "("+str(i+1)+", "+str(num[i].index(row_max)+1)+")"
    row_min = min(num[i])
    row_min_pos = "("+str(i+1)+", "+str(num[i].index(row_min)+1)+")"
    print("\nRow #",i+1,
    "\nHighest element is",row_max,"occurs at location",row_max_pos,
    "\nLowest element is",row_min,"occurs at location",row_min_pos,"\n")

for i in range(c):
    column = [col[i] for col in num]
    col_max = max(column )
    col_max_pos = "("+str(column.index(col_max)+1)+", "+str(i+1)+")"
    col_min = min(column)
    col_min_pos = "("+str(column.index(col_min)+1)+", "+str(i+1)+")"
    print("\nColumn #",i+1,
    "\nHighest element is",col_max,"occurs at location",col_max_pos,
    "\nLowest element is",col_min,"occurs at location",col_min_pos,"\n")