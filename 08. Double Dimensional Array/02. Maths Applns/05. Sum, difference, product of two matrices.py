import os
os.system("cls")

def displayMatrix(num): 
    for i in range(len(num)):
        for j in range(len(num[0])):
            print(num[i][j],"\t",end="")
        print()

def sumOfMatrix(num1, num2):
    return [[num1[i][j]+num2[i][j] for j in range(len(num2[0]))] for i in range(len(num1))]
    
def diffOfMatrix(num1, num2):
    return [[num1[i][j]-num2[i][j] for j in range(len(num2[0]))] for i in range(len(num1))]

def prodOfMatrix(num1, num2):
    prod = [[0]*len(num1[0]) for i in range(len(num1))]
    for i in range(len(num1)):
        for j in range(len(num2[0])):
            for k in range(len(num1[0])):
                prod[i][j]+= num1[i][k]*num2[k][j]
    return prod

print("To find the sum, difference and product of two conformable matrices")
r1 = int(input("Enter the number of rows of matrix 1: "))
c1 = int(input("Enter the number of columns of matrix 1: "))
r2 = int(input("Enter the number of rows of matrix 2: "))
c2 = int(input("Enter the number of columns of matrix 2: "))

if r1==r2 and c1==c2 or c1==r2:
    num1, num2 = [[0]*c1 for i in range(r1)], [[0]*c2 for i in range(r2)]
    print("\nEnter elements of the First Matrix:")
    for i in range(r1):
        for j in range(c1):
            print("Enter element at position ("+str(i+1),", "+str(j+1)+"): ", end='', sep='')
            num1[i][j] = int(input())
    print("\nEnter elements of the Second Matrix:")
    for i in range(r2):
        for j in range(c2):
            print("Enter element at position ("+str(i+1),", "+str(j+1)+"): ", end='', sep='')
            num2[i][j] = int(input())
    
    print("\nFirst matrix:")
    displayMatrix(num1)
    print("\nSecond matrix:")
    displayMatrix(num2)
    
    if r1==r2 and c1==c2:
        print("\nSummation matrix:")
        displayMatrix(sumOfMatrix(num1,num2))
        print("\nDifference matrix:")
        displayMatrix(diffOfMatrix(num1,num2))
    else:
        print("\nSorry! The dimensions of the given matrices are incompatible for addition/subtraction.")
    if c1==r2:
        print("\nProduct matrix:")
        displayMatrix(prodOfMatrix(num1,num2))
    else:
        print("\nSorry! The dimensions of the given matrices are incompatible for multiplication.")
    print()
else:
    print("\nSorry! The dimensions of the given matrices are incompatible for addition/subtraction/multiplication.")
