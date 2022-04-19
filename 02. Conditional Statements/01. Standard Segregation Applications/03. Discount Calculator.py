'''To calculate discount based on purchase amount'''

print("To compute the discount based on purchase amount:")
amount = float(input("Enter the purchase amount: Rs "))

if amount <= 2000:
	discount = 0.05*amount
elif amount <= 5000:
	discount = 0.1*amount
elif amount <= 10000:
	discount = 0.15*amount
else:
	discount = 0.2*amount

print("\nPurchase amount: Rs ",amount,
	"\nDiscount: Rs ", discount)