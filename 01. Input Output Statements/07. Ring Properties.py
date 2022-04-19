'''To calculate area and circumference of ring'''

print("To calculate area and circumference of ring:")
outer_rad = float(input("Enter outer_rad radius of ring: "))
inner_rad = float(input("Enter inner_rad radius of ring: "))

circum = 2*(22/7) * (outer_rad - inner_rad)
area =  (22/7)* ((outer_rad**2) - (inner_rad**2))

print("\nCircumference: ",round(circum,3),
	"\nArea: ", round(area,3))



# Well Done!!