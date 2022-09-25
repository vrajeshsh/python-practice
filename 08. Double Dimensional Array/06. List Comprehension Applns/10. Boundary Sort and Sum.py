import os
os.system("cls")

def displayMatrix(num):
    for i in range(r):
        for j in range(c):
            print(num[i][j],"\t",end="")
        print()

def getBoundarySum(num, r, c):
    return sum([num[i][j] for i in range(r) for j in range(c) if i==0 or i==r-1 or j==0 or j==c-1])

def showBoundary(num, r, c):
    for i in range(r):
        for j in range(c):
            if i==0 or i==r-1 or j==0 or j==c-1:
                print(num[i][j],"\t", end='')
            else:
                print("\t", end='')
        print()               

def getSortedBoundary(num, r, c):
    rearranged = sorted([num[i][j] for i in range(r) for j in range(c) if i==0 or i==r-1 or j==0 or j==c-1])
    # Put the sorted elements BACK to the new matrix and return it in the same way as the 
    # sorted functions done in the sort rows, 
    k, n = 0, len(rearranged)-1
    new2D = [row[:] for row in num]
    for i in range(r):
        for j in range(c):
            if i==0 or j==c-1:
                new2D[i][j] = rearranged[k]
                k+=1
            elif i==r-1 or j==0:
                new2D[i][j]=rearranged[n]
                n-=1
            
    return new2D

print("To sort the outer elements of a matrix and calculate their sum:")
r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))
print()

num = [[0]*c for i in range(r)]

for i in range(r):
    for j in range(c):
        print("Enter integer for element at (",
            str(i+1)+", "+str(j+1)+"): ", end= "", sep= "")
        num[i][j] = int(input())

print("\nThe elements of the 2-D array as given:")
displayMatrix(num)
print("\nThe boundary elements of the original 2-D array:")
showBoundary(num, r, c)
print("\nThe boundary elements of the rearraged 2-D array:")
displayMatrix(getSortedBoundary(num, r, c))
print("\n\nSum of outer row and column elements =",getBoundarySum(num, r,c),"\n")

''' 
One of the algorithms to solve this is:
1. Take a copy of the given 2D matrix as usual.
2. Convert the boundary elements to a 1-D array using Fantabulous technique
3. Sort it and put back its elements in the new 2-D array.
That's it

Try the same technique for the Non-Boundary too!!
'''

#Run and see if it runs successfully. Inform me when done after fixing if required.