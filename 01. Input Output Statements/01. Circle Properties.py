""" A program to calculate the area, perimeter and longest side of a Circle """

print("To find the properties of a Circle:")
rad = float(input("Enter the radius: "))

area = 3.14 * rad * rad
peri = 2* 3.14 * rad
diam = 2* rad

print("\nArea of the circle: ", round(area,3),
	"\nIts perimeter:  ", round(peri,3),
	"\nIts lngest side: ", round(diam, 3))
