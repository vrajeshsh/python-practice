'''To calculate discount and net amount based on gross amount'''

print("To compute the discount and net amount based on gross amount:")
amount = float(input("Enter the purchase amount: Rs "))

if(amount<=500):
	discount = 0
if(amount<=1000):
	discount = 0.1*amount
elif(amount<=2000):
	discount = 0.15*amount
else:
	discount = 0.2*amount
net = amount - discount

print("\nGross Amount: Rs.",amount,
	"\nDiscount: Rs.", discount,
	"\nNet Amount payable: Rs.",net, sep='')