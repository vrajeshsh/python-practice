import os
os.system("cls")

print("To display the Transpose of a given matrix: ")
r = int(input("Enter the number of rows: "))
c = int(input("Enter number of columns: "))
print()

num = []
for i in range(r):
    _ = []
    for j in range(c):
        elem = int(input("Enter element for row #"+str(i+1)+" and column #"+str(j+1)+": "))
        _.append(elem)
    num.append(_)

T = []
for i in range(c):
    row = []
    for j in range(r):
       row.append(num[j][i])
    T.append(row)
    print()

print("\nThe elements of the 2-D array: ")
for i in range(r):
    for j in range(c):
        print(num[i][j],"\t",end="")
    print()
# Two times the SAME CODE, and tat too in 2022?    
print("\nThe transpose of the matrix: ")
for i in range(c):
    for j in range(r):
        print(T[i][j],"\t",end="")
    print()
print()
