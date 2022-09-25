import os
os.system("cls")

print("To display the highest and lowest elements in the diagonals: ")
n = int(input("Enter number of rows / columns: "))
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

maxi, mini, min_loc, max_loc, max_pos, min_pos = num[0][0], num[0][0], "Left diagonal", "Left diagonal", "(1, 1)", "(1, 1)"
for i in range(n):
    if num[i][i]>maxi:
        maxi = num[i][i]
        max_loc = "Left diagonal"
        max_pos = "("+str(i+1)+", "+str(i+1)+")"
    elif num[i][n-i-1]>maxi:
        maxi = num[i][n-i-1]
        max_loc = "Right diagonal"
        max_pos = "("+str(i+1)+", "+str(n-i)+")"
    if num[i][i]<mini:
        mini = num[i][i]
        min_loc = "Left diagonal"
        min_pos = "("+str(i+1)+", "+str(i+1)+")"
    elif num[i][n-i-1]<mini:
        mini = num[i][n-i-1]
        min_loc = "Right diagonal"
        min_pos = "("+str(i+1)+", "+str(n-i)+")"

print("\nELEMENT TYPE\tVALUE\t\tPRESENT IN\tCOORDINATE\nHighest\t\t",maxi,"\t\t",
    max_loc, "\t",max_pos,"\nLowest\t\t",mini,"\t\t",min_loc,"\t",min_pos,"\n",sep='' )

# Wait till the next topic comes.... that should change COMPLETELY (at least expected) your Java style of
# coding as you often do.
