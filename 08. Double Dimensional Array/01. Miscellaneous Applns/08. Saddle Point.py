import os
os.system("cls")

print("To check if saddle point exist in the 2-D matrix:")
r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))
print()

num = []
for i in range(r):
    _ = []
    for j in range(c):
        elem = int(input("Enter element for row #"+str(i+1)+" and column #"+str(j+1)+": "))
        _.append(elem)
    num.append(_)

print("\nThe elements of the 2-D array:")
for i in range(r):
    for j in range(c):
        print(num[i][j],"\t", end='')
    print()

sp=""
# for i in range(r):
#     row_min, col_pos = num[i][0], 0
#     for j in range(c):
#         if num[i][j] < row_min:
#             row_min = num[i][j]
#             col_pos = j
#     col_max = num[0][col_pos]
#     for k in range(r):
#         if num[k][col_pos] > col_max:
#             col_max = num[k][col_max]
#     if row_min==col_max:
#         sp+="("+str(i)+", "+str(j)+")"

for i in range(r):
    row_min, col_pos = num[i][0]
        
if sp:
    print("\nSaddle point ",sp," exists at location ",col_pos,"\n",sep='')
else:
    print("\nNo Saddle Point exists in the matrix!\n")

'''
You need to print the locations also as in (row_index, col-index) e.g. (3, 2) along with the Saddle Point.
Remember mathematically you can get only ONE SADDLE POINT in a matrix. But the same can occur at 
different locations in the matrix.

'''