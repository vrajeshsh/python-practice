'''To calculate the Cost, Discount and Payable Amount of Computers & Printers'''

print("To calculate the Cost, Discount and Payable Amount of Computers & Printers:")
price_lap= float(input("Enter the price of a computer: Rs "))
x = int(input("Enter number of laptops purchased: "))
price_print= float(input("\nEnter the price of a printer: Rs "))
y = int(input("Enter number of printers purchased: "))

cost_lap = price_lap*x				# calc the total cose of laptops
discount_lap = .15*cost_lap
amount_lap = .85*cost_lap   

cost_print = price_print*y
discount_print = .1*cost_print
amount_print = .9*cost_print  

print("\nTotal cost: Rs ", (cost_lap+cost_print),
	"\nDiscount: Rs ", (discount_print+discount_lap),
	"\nPayable Amount: Rs ",(amount_print+amount_lap))
