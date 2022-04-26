'''Try to prove Goldbach's conjecture of an integer'''
print("Try to prove Goldbach's conjecture of an integer:")
num = int(input("Enter a number: "))

con=""

for i in range(2,num-1):
	count1,count2=0,0
	for j in range(2,i):
		if i%j==0:
			count1+=1
	if count1==0:
		for j in range(2,num-i):
			if (num-i)%j==0:
				count2+=1
		if count2==0:
			con= (num-i),"+",i

print("\n",num," = ",con,sep='')