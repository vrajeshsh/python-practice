'''To generate the Prime Factors of a number'''

print("To generate the Prime Factors of a number")
num = int(input("Enter a number: "))

facs = ""

for i in range(2, num//2+1):
	if num%i==0:
		isFound= False
		for j in range(2, i//2+1):
			if i%j==0:
				isFound= True
				break
		if not isFound: 
			facs+=str(i) if facs=="" else ", "+str(i)

if facs == "":
	print("\n",num,"is Prime thus has no factors.")
else:
	print("\nPrime Factors of",num,": ",facs) 