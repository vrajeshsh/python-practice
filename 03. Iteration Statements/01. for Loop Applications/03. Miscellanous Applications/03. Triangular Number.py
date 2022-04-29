'''To display all Triangular numbers till n'''

print("To display all Triangular numbers till a limit:")
n = int(input("Enter the limit: "))

print("\nTriangular Number till",n,":\n")
triNum = 0
for i in range(1, n+1):
	triNum+= i
	if triNum <= n:
	    print(triNum if i==1 else ", " + str(triNum), end='')
