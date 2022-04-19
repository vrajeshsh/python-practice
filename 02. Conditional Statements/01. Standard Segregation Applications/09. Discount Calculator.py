'''To calculate discount based on purchase amount and type of cloth'''

print("To calculate discount based on purchase amount on type of cloth:")
amount = float(input("Enter the purchase amount: Rs "))
cloth  = input("Enter the type of Cloth [M / H]: ")

if amount < 1000:
	disc_rate = 2 if cloth == "M" or cloth == "m" else 5
elif amount < 5000:
	disc_rate = 20 if cloth == "M" or cloth == "m" else 25
elif amount < 10000:
	disc_rate = 40 if cloth == "M" or cloth == "m" else 50
else:
	disc_rate = 50 if cloth == "M" or cloth == "m" else 60

discount = (disc_rate/100)*amount
net = amount-discount

print("\n\t\t\tBombay Dying\n\tTax-Cum-Invoice for Cloth Sales",
	"\n\nPurchase Amount\t\t:\tRs",amount,
	"\nDiscount Enjoyed\t:\tRs",round(discount,2),
	"\nNet Payable Amount\t:\tRs",round(net,2),
	"\n\nTHANK YOU! Please VISIT US again!")
