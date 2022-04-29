'''To calculate the Primorial value of an integer'''

print("To calculate the Primorial value of an integer:")
num = int(input("Enter the integer: "))

facs,prod='',1

for i in range(2,num+1):
	isPrime=False
	for j in range(2,i):
		if i%j==0:
			isPrime=True
			break
	if not isPrime:
		facs+= str(i) if facs=="" else " x "+str(i)
		prod*=i

if facs=="":
	print("\nPlease enter an even integer greater than 2")
else:
	print("\n",num,"# = ",facs," = ",prod,sep='')
