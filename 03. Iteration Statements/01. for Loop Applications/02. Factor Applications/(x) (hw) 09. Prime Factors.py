'''To generate the Prime Factors of a number'''

print("To generate the Prime Factors of a number")
num = int(input("Enter a number: "))

facs,temp="",num

for i in range(2,num//2+1):
	count=0
	for j in range(2,i):
		if i%j==0:
			count+=1
	if count==0 and temp%i==0:
		temp/=i
		facs+=str(i) if facs=="" else ", "+str(i)

print("\nPrime Factors of",num,": ",facs)