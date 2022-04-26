'''To generate all prime Fibonacci within an inteval'''

print("To generate all prime Fibonacci within an inteval:")
l_limit = int(input("Enter lower limit: "))
u_limit = int(input("Enter upper limit: "))

a, b,fib,ssum= 0,1,"",0


for i in range(2,u_limit):
	ssum = a+b
	a = b
	b = ssum
	count=0
	for j in range (2,i):
		if i%j==0:
			count+=1
	if count==0 and l_limit<=ssum<=u_limit:
		fib+=str(ssum) if fib=="" else ", "+str(ssum)
	

print("\nPrime Fibonacci numbers between",l_limit,"and",u_limit,": ",fib)

# check outer loop