'''To solve Simultaneous Equations'''

print("To solve Simultaneous Equations, enter the six coefficients below:")
print("\t\t\tax + by = m\n\t\t\tcx + dy = n\n")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
d = float(input("d: "))
m = float(input("m: "))
n = float(input("n: "))

denom = a * d - c * b
if denom != 0:
	x = (m * d - b * n)/denom
	y = (n * a - m * c)/denom

if denom !=0:
	print("\nSolution:\nx: ",x,"\ny: ",y)
else:
	print("\nDenominator cannot be zero!")
