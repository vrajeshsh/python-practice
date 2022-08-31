import os
os.system("cls")

print("To form a table from Fibonacci numbers:")
r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

matrix, a, b = [[0]*c for i in range(r)], -1, 1

for i in range(r):
    for j in range(c):
        ssum = a + b
        a, b = b, ssum
        matrix[i][j]= ssum

print("\nThe natural Fibonacci numbers as filled in 2-D array are:")
for i in range(r):
    for j in range(c):
        print(matrix[i][j],"\t", end='')
    print()
print()
