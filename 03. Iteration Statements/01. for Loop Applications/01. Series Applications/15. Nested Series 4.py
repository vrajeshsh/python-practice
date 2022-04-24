'''x!/10 + (x+2)!/15! + (x+4)!/20 .... (x+n)!/m'''

print("To generate the Sequential Series: x!/10 + (x+2)!/15 + (x+4)!/20 .... (x+n)!/m: ")
n = int(input("\nEnter number of terms: "))
x = int(input("Enter the value of 'x': "))

ssum, m = 0, 5		# added 'm' here and assigned 5 to it

print ("\nThe Factorial Series till limiting index",n,":")
for i in range(0, n+1, 2):		# fixed the loop
	fact = 1
	for j in range(1, x+i+1):	# fixed this loop too
		fact*=j
	m+= 5
	term = fact/m
	ssum+=term
	print(term if i==0 else " + "+str(term), end='')

print("\n\nSum of the series: ",round(ssum,3))
