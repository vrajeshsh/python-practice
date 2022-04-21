'''x + (1^2*x^3)/3! + (1^2*3^2*x^5)/5! + (1^2*3^2*5^2*x^7)/7! .... x^n/x!'''

print("To generate the Nested Series: x + (1^2*x^3)/3! + (1^2*3^2*x^5)/5! + (1^2*3^2*5^2*x^7)/7! till n terms: ")
n = int(input("Enter number of terms: "))
x = int(input("Enter the value of 'x': "))

y,num,term,ssum = 1,1,0,1

for i in range(1,n+1):
	fact = 1
	for j in range(1,y+1):
		fact*=j

	
	term = (num*(x**y))/fact
	ssum+=term
	print(term if i==1 else " + "+str(term), end='')
	num*=(y**2)
	y+=2

print("\nSum of the series: ",round(ssum,3))