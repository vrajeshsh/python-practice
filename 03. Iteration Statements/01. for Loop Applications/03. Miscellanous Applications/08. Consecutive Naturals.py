'''To generate all combinations of consecutive naturals that add upto n'''

print("To generate all combinations of consecutive naturals that add upto n:")
n = int(input("Enter a number: "))

ssum,cons,check=0,"",0

# for i in range(1,n+1//2):
# 	ssum+=i
# 	if ssum==n:
# 		for j in range(1,i+1):
# 			cons+=str(j)+" "
# 		cons+="\n"
# 		ssum=0

for i in range(1,n+1//2):
	check=(n-(i*(i+1))/2)/(i+1)
	#print(check)
	if check - int(check) == 0 and check>0:
		for j in range(int(check),n):
			ssum+=j
			cons+=str(j)+" "
			if ssum==n:
				cons+="\n"
				ssum = 0
				break

print("\nAll combinations of consecutive naturals that add upto",n,":\n",cons,sep='')