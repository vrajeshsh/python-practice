'''To calculate commission of a sales employee based on gender and their monthly sales'''

print("To calculate commission of sales employee:")
sex = input("Enter employee's gender [M/F]:")
sale_amt = float(input("Enter their sale for the month: Rs"))

if sale_amt <= 150000:
	comm = 0.1 * sale_amt if sex == 'M' or sex=='m' else 0.12 * sale_amt
elif sale_amt <= 200000:
	comm = 0.14 * sale_amt if sex == 'M' or sex=='m' else 0.16 * sale_amt
else:
	comm = 0.18 * sale_amt if sex == 'M' or sex=='m' else 0.2 * sale_amt
	
total = 0.1 * sale_amt if sale_amt <= 100000 else 5000 + comm

print("\nCommission\t\t\t\t:\tRs ", comm,
	"\nTotal Monthly Salary\t:\tRs ",total)
