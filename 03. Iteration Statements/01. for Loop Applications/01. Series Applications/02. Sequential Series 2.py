'''0 + 7 + 26 + 63...n'''

print("To generate the Sequential Series: 0 + 7 + 26 + 63... till n terms: ")
n = int(input("Enter number of terms: "))
term, ssum = 0, 0

print("\nThe Sequential Series till",n,"terms: ")
for i in range(1,n+1):
	term=(i**3)-1
	ssum+=term
	print(term if i==1 else " + "+str(term), end='')

print("\nSum of the series: ",ssum)
