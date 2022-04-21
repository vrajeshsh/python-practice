'''1 + x + x^2/2! + x^3/4! + x^4/6!.... x^n/x!'''

print("To generate the Sequential Series: '''1 + x + x^2/2! + x^3/4! .... x^n/x!''': ")
n = int(input("Enter number of terms: "))
x = int(input("Enter the value of 'x': "))

term,ssum = 0,0

for i in range(0,n):
	fact = 1
	for j in range(1,(2*i-1)):
		fact*=j
	term = round(x**i/fact,3)
	ssum+= term
	print(term if i==0 else " + "+str(term), end='')

print("\n\nSum of the series: ",round(ssum,3))