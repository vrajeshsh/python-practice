import os
os.system("cls")

print("To form a matrix using triangular numbers in reverse order:")
r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

matrix, num, count= [[0]*c for i in range(r)], 0, 1

for i in range(c-1, -1, -1):
    for j in range(r-1, -1, -1):
        num+=count
        matrix[j][i] = num
        count+=1

print("\nThe Triangular numbers as filled columnwise in the 2-D array are:")
for i in range(r):
    for j in range(c):
        print(matrix[i][j],"\t", end='')
    print()
print()