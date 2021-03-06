'''1 + x/1! + x^3/2! + x^5/3! .... x^(2*n-1)/n!'''

print("To generate the Sequential Series: 1 + x/1! + x^3/2! + x^5/3! .... x^(2*n-1)/n!: ")
n = int(input("\nEnter the limiting index: "))
x = int(input("Enter the value of 'x': "))

ssum = 0

print ("\nThe Factorial Series till limiting index",n,":")
for i in range(1, n+1):
	fact = 1
	for j in range(1,i+1):
		fact*=j
	term = x**(2*i-1)/fact
	ssum+=term
	print(term if i==1 else " + "+str(round(term, 2)), end='')

print("\nSum of the series: ",round(ssum,3))