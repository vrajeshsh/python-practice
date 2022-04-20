'''1 + 12 + 123 + 1234 + 12345...n'''

print("To generate the Sequential Series: 1 + 12 + 123 + 1234 + 12345... till n terms: ")
n = int(input("Enter number of iterations: "))
term,ssum=0,0

print("\nThe Sequential Series till",n,"terms: ")
for i in range(1,n+1):
	term=(term*10)+i
	ssum+=term
	print(term if i==1 else " + "+str(term), end='')
	
print("\nSum of the series: ",ssum)