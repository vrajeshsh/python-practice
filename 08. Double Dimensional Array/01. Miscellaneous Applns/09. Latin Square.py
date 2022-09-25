import os
os.system("cls")

def isLatinSquare(num):
    for i in range(n):
        for j in range(n):
            if num[i].count(num[i][j])>1:
                return False
            for k in range(i+1, n):
                if num[i][j]==num[k][j]:
                    return False
    return True

print("To check if give 2-D matrix is a Latin Square:")
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


if isLatinSquare(num):
    print("\nThe given matrix is a Latin Square.\n")
else:
    print("\nThe given matrix is NOT a Latin square.\n")
