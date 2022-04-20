'''1 + 2 + 4 + 8...n'''

print("To generate the Sequential Series: 1 + 2 + 4 + 8... till n terms: ")
n = int(input("Enter number of terms: "))

term, ssum = 0, 0

print("\nThe Sequential Series till",n,"terms: ")
for i in range(0, n+1):
	term= 2**i
	ssum+= term
	print(term if i==0 else " + "+str(term), end='')

print("\nSum of the series: ",ssum)
