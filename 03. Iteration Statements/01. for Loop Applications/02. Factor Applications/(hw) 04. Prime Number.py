'''Check whether a number is Prime or not'''

print("To check whether a number is Prime or not")
num = int(input("Enter a number: "))

count=0
for i in range(2,num//2+1):
	if num%i==0:
		count+=1

print("\n",num, " is" ,("" if count==0 and num<2 else " NOT"), 
	" a Prime number.", sep='')

