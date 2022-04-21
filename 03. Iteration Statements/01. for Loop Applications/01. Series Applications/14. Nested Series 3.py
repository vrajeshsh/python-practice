'''1 - x^2/2! + x^4/4!  - x^6/6.... x^n/n!'''

print("To generate the Sequential Series: 1 - x^2/2! + x^4/4!  - x^6/6.... x^n/n!: ")
n = int(input("Enter number of terms: "))
x = int(input("Enter the value of 'x': "))

y,sign,term,ssum = 2,1,0,1

for i in range(1,n):
	fact = 1
	for j in range(1,y+1):
		fact*=j

	sign*=-1
	term = (sign*(x**y))/fact
	ssum+=term
	print(term if i==1 else (" - "+str(term) if sign<0 else " + "+str(term)), end='')
	y+=2

print("\nSum of the series: ",round(ssum,3))