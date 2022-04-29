'''To generate multiplication table till n'''
print("To generate multiplication table till n:")
n=int(input("Enter a number: "))

prod,temp="",0
for i in range(1,n+1):
	prod+="\n"+str(i)+"\t|\t"
	for j in range(1,13):
		prod+=str(i*j)+"\t"
	
	
print("\n*\t|\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12")
print("-------------------------------------------------------")
print("\t",prod)