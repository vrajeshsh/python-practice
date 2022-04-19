'''To generate compute bill based on the number of years of dealing and number of computers purchased'''

print("To generate the bill for a customer purchasing computer hardware:")
comp_qnty = int(input("Enter the no. of computers purchased: "))
yrs = float(input("Enter no. of years of business: "))

if comp_qnty < 20:
	unit_cost = 28000 
elif comp_qnty < 40:
	unit_cost = 25000
else:
	unit_cost = 20000

comp_cost = unit_cost * comp_qnty

if yrs > 5:
	discount = 0.1 * comp_cost
else:
	discount = 0

net = comp_cost-discount

print("\n\t\tHI-Tech Computer Solutions\n\tTax-Cum-Invoice for Computer Hardware Sales\n\nITEM DESC\t\tQNTY\tUNIT PRICE\nComputer PC\t\t",
	comp_qnty,"\t",unit_cost,"\n\nTotal Cost\t\t\t:\tRs",round(comp_cost,2),
	"\nDiscount Enjoyed\t:\tRs",round(discount,2),
	"\nNet Payable Amount\t:\tRs",round(net,2),
	"\n\n\t\tTHANK YOU! Please VISIT US again!")
