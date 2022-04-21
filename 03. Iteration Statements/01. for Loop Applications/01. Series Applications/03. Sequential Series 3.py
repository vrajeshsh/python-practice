'''1 - x^2 + x^4 - x^6...n'''

print("To generate the Sequential Series: 1 - x^2 + x^4 - x^6... till n terms: ")
n = int(input("Enter number of terms: "))
x = int(input("Enter the value of 'x': "))

sign, term, ssum=1,0,0
print("\nThe Sequential Series till",n,"terms: ")
for i in range(n):
	term=(x**(i*2))
	ssum+=term *sign
	print(term if i==0 else (" - "+str(term) if sign<0 else " + "+str(term)), end='')
	sign*=-1
	
print("\nSum of the series: ",ssum)

