'''1 + 11 + 111 + 1111 + 11111...n'''

print("To generate the Sequential Series: 1 + 11 + 111 + 1111 + 11111... till n terms: ")
n = int(input("Enter number of terms: "))
term, ssum=0,0

print("\nThe Sequential Series till",n,"terms: ")
for i in range(n):
	term=(term*10)+1
	ssum+=term
	print(term if i==0 else " + "+str(term), end='')

print("\nSum of the series: ",ssum)

