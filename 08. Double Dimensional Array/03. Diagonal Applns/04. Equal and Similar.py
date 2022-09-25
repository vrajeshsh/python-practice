import os
os.system("cls")

def getType(num):
    isEqual = True
    for i in range(n):
        isSimilar = False
        if num[i][i] != num[i][n-i-1]:
            isEqual = False
    # Fix the 'Similar' part. It's incorrectly done currently. Fix the code 
    # considering the sample I/O given at the end of this program.
        for j in range(n):
            if num[i][i]==num[j][n-j-1]:
                isSimilar = True # (Consider: Just if one element becomes equal, then True, whatif the others are not?)
        if not isSimilar:
            break
    if isEqual:
        return "Equal and Similar"
    elif isSimilar:
        return "Similar"
    else:   
        return "Neither Equal nor Similar"

print("To check if the diagonals of a matrix are equal and similar: ")
n = int(input("Enter the number of rows/columns: "))
print()

num = [[0]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        print("Enter integer for element at (",
            str(i+1)+", "+str(j+1)+"): ", end= "", sep= "")
        num[i][j] = int(input())    

print("\nThe elements of the 2-D square matrix: ")
for i in range(n):
    for j in range(n):
        print(num[i][j],"\t",end="")
    print()

print("\nThe diagonals of the given array are",getType(num),"!\n")

#You keep them FIXED... will check tomorrow...
'''
1   2   3   1
5   2   2   8
9   2   1  12
2  14   15  2

Since the frequencies of the diagonal elements are NOT SAME, therefore
the diagonals are considered NOT SIMILAR!!
'''