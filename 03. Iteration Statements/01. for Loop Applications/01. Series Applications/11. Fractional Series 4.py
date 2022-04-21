'''1/3 + 8/5 + 27/7 + 64/9...n'''

print("To generate the Sequential Series: 1/3 + 8/5 + 27/7 + 64/9... till n terms: ")
n = int(input("Enter number of terms: "))
term,ssum=0,0

print("\nThe Fractional Series till",n,"terms: ")
for i in range(1,n+1):
	term=round((i**3)/(2*i+1),3)
	ssum+=term
	print(term if i==1 else " + "+str(term), end='')
	
print("\nSum of the series: ", round(ssum,3))