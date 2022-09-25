import os
os.system("cls")

def isIdentity(num, n):
    for i in range(n):
        for j in range(n):
            if (i==j and num[i][j]!=1) or (i!=j and num[i][j]!=0):
                return False
    return True

print("To check whether or the given matrix is an Identity Matrix")
n = int(input("Enter number of rows/columns: "))

num = []
for i in range(n):
    _ = []
    for j in range(n):
        elem = int(input("Enter element for row #"+str(i+1)+" and column #"+str(j+1)+": "))
        _.append(elem)
    num.append(_)

print("\nThe elements of the 2-D array: ")
for i in range(n):
    for j in range(n):
        print(num[i][j],"\t",end="")
    print()

if isIdentity(num, n):
    print("\nThe given matrix is an Identity Matrix!\n")
else:
    print("\nThe given matrix is NOT an Identity Matrix!\n")
