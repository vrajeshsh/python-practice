'''To generate the Tribonacci seies till n'''

print("To generate the Tribonacci seies till n:")
n = int(input("Enter the limit: "))

a,b,c,trib = 0,0,1,""

for i in range(3,n):
	d = a+b+c
	a=b
	b=c
	c=d
	if d<=n:
		trib+=", "+str(d)

print("\nTribonacci Series till ",n,":\n0, 1",trib,sep='')