'''To calculate the area and Perimeter of Triangle'''

print("To calculate the Area and Perimeter of a Triangle:")
a = float(input("Enter its 1st side : "))
b = float(input("Enter its 2nd side : "))
c = float(input("Enter its 3rd side : "))

peri = a + b + c
s = peri/2
area = (s*(s-a)*(s-b)*(s-c))**0.5	# good you know it

print("\nThe Area of Triangle :", round(area,3),
	"\nIts Perimeter : ", round(peri,3))