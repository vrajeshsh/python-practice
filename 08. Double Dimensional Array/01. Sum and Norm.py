import os
from shutil import which
os.system("cls")

print("To find the sum and norm of all elements in a table formed by using the formula i^3+j^3:")
row = int(input("Enter number of rows: "))
col = int(input("Enter number of columns: "))

ssum, norm, T = 0, 0, []

for i in range(0, row):
    _ = []
    for j in range(0, col):
        _.append((i+1)**3 + (j+1)**3)
    T.append(_)

print("\nThe numeric table as formed by using the formula i^3 + j^3:")
for i in range(0, row):
    for j in range(0, col):
        print(T[i][j],"\t",end='')
        norm+= T[i][j]**2
        ssum+= T[i][j] if i==j and i%2==1 else 0
    print()
norm = round(norm**0.5, 3)

print("Sum of the table: ", ssum,
    "\nNorm of the table: ",norm,"\n",sep='')

# I generally tend to fix only the algorithm decided by the student in the first instance
# So fixed it how you thought of it.
# Although there are better ways to do this program, which perhaps you will realize and learn in some
# other assignment when you will be forced to think the other way... 

# True, with the append() way, this is how one can fill a 2-D array/list