'''Check whether a number is perfect or not'''

print("Check whether a number is perfect or not")
num = int(input("Enter a number: "))

fsum = 0
for i in range(1,num//2+1):
	if num%i==0:
		fsum+=i

print("\n",num, " is" ,("" if fsum==num else " NOT"), 
	" a Perfect number.", sep='')
