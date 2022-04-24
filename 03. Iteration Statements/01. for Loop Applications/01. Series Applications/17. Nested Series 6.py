'''x + (1^2*x^3)/3! + (1^2*3^2*x^5)/5! + (1^2*3^2*5^2*x^7)/7! .... x^n/x!'''

print("To generate the Nested Series: x + (1^2*x^3)/3! + (1^2*3^2*x^5)/5! + (1^2*3^2*5^2*x^7)/7! till n terms: ")
n = int(input("\nEnter the no. of terms: "))
x = int(input("Enter the value of 'x': "))

ssum = 0

print ("\nThe Exponent Series till limiting denominator",n,": ")
for i in range(1, 2*n+1, 2):	# generating 'n' terms here
	fact, num = 1, 1
	for j in range(1, i+1):
		fact*= j				# calc the deniminator gere
	for j in range(1, i, 2):
		num*= j					# calc the numerrator here
	term = num*x**i/fact
	ssum+= term
	print(term if i==1 else " + "+str(round(term, 3)), end='')
	
print("\nSum of the series: ",round(ssum,3))