'''(1+2)/(1*2) + (1+2+3)/(1*2*3) + ... + (1+2+3+4+...+n)/(1*2*3*4*...*n)'''

print("To generate the Sequential Series: (1+2)/(1*2) + (1+2+3)/(1*2*3) + ... + (1+2+3+4+...+n)/(1*2*3*4*...*n): ")
n = int(input("Enter number of terms: "))

term,ssum = 0,0

for i in range(1,n+1):
	num,denom=0,1
	for j in range(1,i+2):
		num+=j
		denom*=j
		
	term = round(num/denom,3)
	ssum+= term
	print(term if i==1 else " + "+str(term), end='')

print("\n\nSum of the series: ",round(ssum,3))
