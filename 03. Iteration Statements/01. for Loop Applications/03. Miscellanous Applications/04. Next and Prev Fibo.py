'''To generate the next and previous fibonacci number afetr n'''
print("To generate the next and previous fibonacci number after n:")
n = int(input("Enter a number: "))

a,b=0,1
for i in range(2,n):
	c=a+b
	a=b
	b=c
	if c>n:
		nxt=c
		prv = (a+b)-c
		break

print("\nThe next Fibonacci number after",n,"is"
	,nxt,"\nThe previous Fibonacci number before",n,"is",prv)