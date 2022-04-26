'''To calculate the Primorial value of an integer'''

print("To calculate the Primorial value of an integer:")
num = int(input("Enter a number: "))

facs=''

for i in range(2,num+1):
	count=0
	for j in range(2,i):
		if i%j==0:
			count+=1
	if count==0:
		facs+= str(i) if facs=="" else ", "+str(i)

print("\n",num,"# = ",facs,sep='')
