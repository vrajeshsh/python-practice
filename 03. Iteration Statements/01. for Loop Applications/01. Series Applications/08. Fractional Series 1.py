'''1/(1*2*3) + 1/(2*3*4) + 1/(3*4*5)...1/(n*(n-2)*(n-1))'''

print("1/(1*2*3) + 1/(2*3*4) + 1/(3*4*5)...1/(n*(n-2)*(n-1))")
n = int(input("Enter number of terms: "))
term,ssum=0,0

print("\nThe Sequential Series till",n,"terms: ")
for i in range(1,n+1):
	term=round(1/(i*(i+1)*(i+2)),2)
	ssum+=term
	print(term if i==1 else " + "+str(term), end='')
	
print("\nSum of the series: ",ssum)