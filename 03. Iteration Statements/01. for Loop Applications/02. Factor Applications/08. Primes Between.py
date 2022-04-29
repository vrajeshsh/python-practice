'''To generate all prime numbers between a limit'''
print("To generate all prime numbers between a limit")
s_limit = int(input("Enter start limit: "))
e_limit = int(input("Enter end limit: "))

facs=""

for i in range(s_limit, e_limit+1):
	if i>1:
		isFound = False
		for j in range(2,i//2+1):
			if i%j==0:
				isFound= True
				break			# this speedens up the process...
		if not isFound:	
			facs+= str(i) if facs=="" else ", "+str(i)

if facs =="":
	print("\nThere are no prime numbers between ",s_limit," and ",e_limit,".", sep='')
else:
	print("\nPrime numbers between ",s_limit," and ",e_limit," are:\n",facs,sep='')
