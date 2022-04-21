'''1/2 + 3/4 + 5/6 + 7/8...n'''

print("To generate the Sequential Series: 1/2 + 3/4 + 5/6 + 7/8... till n terms: ")
n = int(input("Enter number of terms: "))
temp,term,ssum=1,0,0

print("\nThe Fractional Series till",n,"terms: ")
for i in range(1,n+1):
	term=round(temp/(temp+1),4)
	ssum+=term
	print(term if i==1 else " + "+str(term), end='')
	temp+= 2

print("\nSum of the series: ",ssum) 