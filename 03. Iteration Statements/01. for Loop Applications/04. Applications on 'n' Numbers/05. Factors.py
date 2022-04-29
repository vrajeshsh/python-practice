'''To display number that have factors between 1 and 6. Also calculate sum and count'''

print("To display number that have factors between 1 and 6. Also calculate sum and count:")
n = int(input("Enter number of numbers: "))

count,ssum,facs=0,0,""

print()

for i in range(1,n+1):
	print("Enter number #",i,": ", sep='', end='')
	num = int(input())

	if num%2==0 and num%3==0 and num%5==0:

		count+=1
		ssum+=num
		facs+= str(num) if facs=="" else ", "+str(num)

print("\nNumbers with factors between 1 and 6: ",facs,
	"\nIt's count: ",count,
	"\nIt's sum: ",ssum)

# Accepted