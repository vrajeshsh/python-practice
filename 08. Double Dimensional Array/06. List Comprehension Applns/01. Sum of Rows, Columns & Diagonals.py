import os
os.system("cls")

print("To find the sum of each row, column, diagonal and total elements of a 2-D matay:")
n = int(input("\nEnter the no. of rows/columns of the square matay: "))

mat, matsum = [[0]*n for i in range(n)], 0 

for i in range(n):
	for j in range(n):
		print("Enter the element in position (", i+1, ",", j+1, "): ", sep = '', end = '')
		mat[i][j] = int(input())

print("\nThe elements in the 2-D matay as as follows:")
for i in range(n):
	for j in range(n):
		print("{:<6d}".format(mat[i][j]), sep = '', end = '')
	print()

leftdiag, rightdiag = [mat[i][i] for i in range(n)], [mat[i][n-1-i] for i in range(n)]

for i in range(n):
	eachrow, eachcol = mat[i], [col[i] for col in mat]
	matsum+= sum(eachrow)
	print("\nSum of row #", (i+1),": ", sum(eachrow),
		"\nSum of column #", (i+1),": ", sum(eachcol), sep='')
print("\nLeft diagonal sum: ", sum(leftdiag),
	"\nRight diagonal sum: ", sum(rightdiag), 
	"\n\nSum of all elements: ", matsum, sep='')

	# Study very very very well the 'Fantabulous technique' and start redoing the program the 
	# Fantastic 4 way...
