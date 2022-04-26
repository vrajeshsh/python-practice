'''To generate all prime numbers between a limit'''
print("To generate all prime numbers between a limit")
s_limit = int(input("Enter start limit: "))
e_limit = int(input("Enter end limit: "))

facs=""

for i in range(s_limit,e_limit+1):
	count=0
	if i>1:
		for j in range(2,i//2+1):
			if i%j==0:
				count+=1
		if count==0:	
			facs+= str(i) if facs=="" else ", "+str(i)

print("\nPrime numbers between ",s_limit," and ",e_limit," are:\n",facs,sep='')
