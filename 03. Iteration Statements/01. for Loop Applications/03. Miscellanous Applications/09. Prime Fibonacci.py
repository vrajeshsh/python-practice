print("To generate all prime Fibonacci within an inteval:")
l_limit = int(input("Enter lower limit: "))
u_limit = int(input("Enter upper limit: "))

prime_fibs, a, b = "", 1, 1

for i in range(2, u_limit):
	c = a + b
	a = b
	b = c
	if c >= l_limit and c <= u_limit: 	
		isprime= True
		for j in range(2, c//2):
			if c%j==0:
				isprime= False
				break
		if isprime:
			prime_fibs+= str(c) if prime_fibs=="" else ", "+str(c)
	
if prime_fibs == "":
	print("\nThere are no prime fibonacci numbers between",l_limit,"and",u_limit)
else:
	print("\nPrime Fibonacci numbers between",l_limit,"and",u_limit,
		":\n",prime_fibs)
