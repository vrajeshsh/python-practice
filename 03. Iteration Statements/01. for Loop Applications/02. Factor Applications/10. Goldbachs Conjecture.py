'''Try to prove Goldbach's nConjecture of an integer'''
print("Try to prove Goldbach's Conjecture of an integer:")
num = int(input("Enter a number: "))

facs=""

if num%2==0 and num>2:
	for i in range(2, num//2+1):
		isPrime= True
		for j in range(2, i//2+1):
			if i%j==0:
				isPrime= False
				break
		if isPrime:
			for j in range(2, (num-i)//2+1):
				if (num-i)%j==0:
					isPrime= False
					break
			if isPrime:
				facs+= "\n"+str(num)+ " = "+str(num-i)+ " + " +  str(i)

if num<2 or facs=="":
	print("\nConjecture not possible. Please enter a number greater than 1")
else:
	print("\nThe Goldbach Primes are: ", facs)