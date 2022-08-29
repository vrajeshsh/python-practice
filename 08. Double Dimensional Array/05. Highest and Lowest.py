from dis import COMPILER_FLAG_NAMES
from distutils.command.check import SilentReporter
import os
from sys import last_traceback
from wsgiref.handlers import BaseCGIHandler
os.system("cls")

print("To print the highest and lowest elemets of each row/column:")
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

for i in range(r):
    row_max, row_min, max_row_pos, min_row_pos = num[i][0], num[i][0], "(1, 1)", "(1, 1)"
    for j in range(c):
        if num[i][j] > row_max:
            row_max = num[i][j]
            max_row_pos = "("+str(i+1)+", "+str(j+1)+")"
        if num[i][j] < row_min:
            row_min = num[i][j]
            min_row_pos = "("+str(i+1)+", "+str(j+1)+")"
    print("\nRow #",i+1,":\n",
    "Highest element is ",row_max," occurs at location: ",max_row_pos,
    "\nLowest element is ",row_min," occurs at location: ",min_row_pos,sep='')

for i in range(c):
    col_max, col_min, max_col_pos, min_col_pos = num[0][i], num[0][i], "(1, 1)", "(1, 1)"  
    for j in range(r):
        if num[j][i] > col_max:
            col_max = num[j][i]
            max_col_pos = "("+str(j+1)+", "+str(i+1)+")"
        if num[j][i] < col_min:
            col_min = num[j][i]
            min_col_pos = "("+str(j+1)+", "+str(i+1)+")"
    print("\nColumn #",i+1,":\n",
    "Highest element is ",col_max," occurs at location: ",max_col_pos,
    "\nLowest element is ",col_min," occurs at location: ",min_col_pos, sep='')
print()
