'''1 + 21 + 321 + 4321 + 54321...n'''

print("To generate the Sequential Series: 1 + 21 + 321 + 4321 + 54321... till n terms: ")
n = int(input("Enter number of terms: "))
term,ssum=0,0

print("\nThe Sequential Series till",n,"terms: ")
for i in range(n):
	term+= (10**i)*(i+1)
	ssum+=term
	print(term if i==0 else " + "+str(term), end='')

print("\nSum of the series:",ssum)