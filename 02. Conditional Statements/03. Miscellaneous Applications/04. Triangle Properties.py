'''To check triangle or not'''

print("To find the properties of a triangle, enter the three sides below:")
a = float(input("Side 1: "))
b = float(input("Side 2: "))
c = float(input("Side 3: "))

if a+b>c and b+c>a and c+a>b:
	s = (a+b+c)/2
	area = (s*(s-a)*(s-b)*(s-c))**0.5

	if a*a==b*b+c*c or c*c==b*b+a*a or b*b==a*a+c*c:
		tri_type = "Right-angled "
	elif a*a>b*b+c*c or c*c>b*b+a*a or b*b>a*a+c*c:
		tri_type = "Obtuse-angled "
	elif a*a<b*b+c*c or c*c<b*b+a*a or b*b<a*a+c*c:
		tri_type = "Acute-angled "
	if a == b== c: 
		tri_type+= "Equilateral"
	elif a == b or b == c or c == a:
		tri_type+= "Isosceles"
	else:
		tri_type+= "Scalene"
	print("\n",tri_type," triangle\nArea: ",round(area,2), sep='')
else:
	print("\nTriangle is NOT POSSIBLE with the given sides!")