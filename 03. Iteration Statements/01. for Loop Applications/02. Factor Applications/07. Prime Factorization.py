''' Write a Python script to accept an integer from the user and then 
display its factors obtained through Prime Factorization.
Consider the following examples:
Prime Factorization of 60:
60 = 2 x 2 x 3 x 5
Prime Factorization of 120:
120 = 2 x 2 x 2 x 3 x 5
'''
print("To generate the Prime Factorization of an integer:")
num = int(input("Enter a number: "))

facs,temp,div= "",num,2

for i in range(num//2+1):
	if temp%div==0:
		temp/=div
		facs+=str(div) if facs=="" else " x "+str(div)
	else:	
		div+=1

if temp==num:
	print("\n",num,"is Prime thus has no factors.")
else:
	print("\nPrime Factorization of",num,": ",facs)
