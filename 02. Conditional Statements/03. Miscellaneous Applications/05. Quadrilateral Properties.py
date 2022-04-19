'''To check kind of Quadrilateral'''

print("To check kind of Quadrilateral:")
a = float(input("Side 1: "))
b = float(input("Side 2: "))
c = float(input("Side 3: "))
d = float(input("Side 4: "))
e = float(input("Angle 1: "))

if a==b==c==d:
	quad_type = "Square" if e==90 else "Rhombus"
elif (a==b and c==d) or (a==c and b==d) or (b==c and a==d):
	quad_type = "Rectangle" if e==90 else "Parallelogram"
else:
	quad_type = "Irregular"

print("\nQuadrilateral Type: ",quad_type)
