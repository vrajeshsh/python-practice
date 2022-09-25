
import os
from re import A
os.system("cls")
# Try to AVOID the append() way of filling up a matrix as far as possible.
# Very soon a fabulous 'short-cut' (like ternary ) will be introduced where the other style ONLY will
# be useful. That is why.
# Change the below code accordingly.
def copyMatrix(num, n):
    temp = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            temp[i][j] = num[i][j]
    return temp

def sortMatrix(num, dir, order):
    if dir==1:
        for i in range(n):
            if order==1:
                num[i].sort()
            elif order==2:
                num[i].sort(reverse = True)
    elif dir==2:
        for i in range(n):
            for j in range(n):
                for k in range(n-i-1):
                    if order==1 and num[k][j] > num[k+1][j] or order==2 and num[k][j] < num[k+1][j]:
                        num[k][j], num[k+1][j] = num[k+1][j], num[k][j]
                            
   

def displayMatrix(num):
    for i in range(n):
        for j in range(n):
            print(num[i][j],"\t",end="")
        print()

ch=''
n = int(input("Enter number of rows/columns: "))
print()

num = [[0]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        print("Enter integer for element at (",
            str(i+1)+", "+str(j+1)+"): ", end= "", sep= "")
        num[i][j] = int(input())    

while ch.lower()!='n':
    print("\nTo globally arrange the elements of a 2-D array:")
    dir = int(input("\nEnter the orientation of arrangement [1. Row-wise 2. Column-wise]: "))
    order = int(input("Enter the order of arrangement [1. Ascending 2. Descending]: "))
    print("\nThe given unsorted elements of the 2-D array are: ")
    displayMatrix(num)

    temp= copyMatrix(num, n)
    
    
    print("\nThe elements of the 2-D array after global sorting: ")
    sortMatrix(temp, dir, order)
    displayMatrix(num)
    ch = input("\nDo you want to try again (Y/N): ")
print()

''' 
There are two algorithms for doing 'Global Sort' of a matrix. Since you have not yet learnt the
'Fantastic algorithm of shortening', therefore that way as of now would be difficult.

Thus go for the slightly lengthy 3-step algorithm which simulates the erstwhile Hero-Honda Ad slogan:
You should visit that old ad once at least:
https://www.youtube.com/watch?v=jx74RYZPpDA&ab_channel=ONLYKUTTS

1. Fill it.     (Convert 2-D to 1-D)
2. Shut it.     (Sort the 1-D)
3. Forget it    (Convert back the sorted 1-D to 2-D)

'''