'''1 - x^2/2! + x^4/4!  - x^6/6.... x^n/n!'''

print("To generate the Sequential Series: 1 - x^2/2! + x^4/4!  - x^6/6.... x^n/n!: ")
n = int(input("\nEnter the limiting index: "))
x = int(input("Enter the value of 'x': "))

sign, ssum = -1, 0		# fixed here: removed y variable

print ("\nThe Exponent Series till limiting index",n,": ")
for i in range(0, n+1, 2):	# fixed here: Generating even indices from 0
	fact = 1
	for j in range(1, i):
		fact*=j
	sign*= -1
	term = x**i/fact	# removed sign from here
	ssum+=term*sign		# and placed it here
	print(term if i==0 else " - "+str(round(term, 2)) if sign<0 \
	 	else " + "+str(round(term, 2)), end='')
	
print("\n\nSum of the series: ",round(ssum,3))

#Accepted after fixing a few mistakes