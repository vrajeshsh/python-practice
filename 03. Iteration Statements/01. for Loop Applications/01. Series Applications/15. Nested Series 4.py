'''x!/10 + (x+2)!/15! + (x+4)!/20 .... (x+n)!/m'''

print("To generate the Sequential Series: x!/10 + (x+2)!/15 + (x+4)!/20 .... (x+n)!/m: ")
n = int(input("Enter number of terms: "))
x = int(input("Enter the value of 'x': "))

term,ssum = 0,0

for i in range(0,n):
	fact = 1
	for j in range(1,(x+(2*i)+1)):
		fact*=j

	term = fact/((i+2)*5)
	ssum+=term
	
	print(term if i==0 else " + "+str(term), end='')

print("\nSum of the series: ",round(ssum,3))
