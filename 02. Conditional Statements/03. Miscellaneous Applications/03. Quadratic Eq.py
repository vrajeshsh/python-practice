'''To solve Quadratic Equations'''
print("To solve a Quadratic Equation, enter the three coefficients below:")
print("\t\t\tax^2 + bx + c = 0\n")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

disc = b*b - 4*a*c
if disc < 0:
	root_type = "Imaginary"
elif disc == 0:
	root1 = root2 = -b/(2*a)
	root_type = "Equal"
else:
	root1 = (-b+(disc**0.5))/2*a
	root2 = (-b-(disc**0.5))/2*a
	root_type = "Real and distinct"

print("\nRoots are: ", root_type)

if disc>=0:		
	print("\nFirst root: ",round(root1,2),
		"\nSecond Root: ",round(root2,2))
