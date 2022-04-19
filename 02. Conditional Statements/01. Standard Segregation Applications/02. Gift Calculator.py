'''To calculate gift based on purchase amount'''

print("To find the gift based on purchase amount:")
amount = float(input("Enter the purchase amount: Rs "))

if amount < 1:
	gift = "Nothing"
elif amount < 1000:
	gift = "Pen"
elif amount < 2000:
	gift = "T-Shirt"
elif amount < 5000:
	gift = "Leather Bag"
else:
	gift = "Watch"


print("\nPurchase Amount: Rs ",amount,
	"\nGift: ",gift)
