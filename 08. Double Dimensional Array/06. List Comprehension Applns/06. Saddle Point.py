import os
os.system("cls")

def lowestinRow(num, r):
    return min(num[r])

def highestInColumn(num, c):
    return max([col[c] for col in num])

def saddlePoint(num):
    loc, sp="", -1
    for i in range(r):
        for j in range(c):
            minInRow, maxInCol = lowestinRow(num, i),  highestInColumn(num, j)
            if  minInRow == maxInCol:
                sp = minInRow
                loc+= ("\n(" if loc=="" else ", (")+str(i+1)+", "+str(j+1)+")" 
    if sp == -1:
        print("\nNo saddle point exists in the matrix!\n")
    else:
        print("\nSaddle Point", sp,"exists in the matrix at location(s):",loc,"\n")

print("The check if Saddle Point exists in a 2-D matrix: ")
r = int(input("Enter number of rows: ")) 
c = int(input("Enter number of columns: ")) 
print()

num = [[0]*c for i in range(r)]
for i in range(r):
    for j in range(c):
        print("Enter element for position (",i+1,", ",j+1,"): ", sep='', end='')
        num[i][j] = int(input())

print("\nThe elements of the 2-D array:")
for i in range(r):
    for j in range(c):
        print(num[i][j],"\t",end='')
    print()

saddlePoint(num)