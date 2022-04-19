'''To calculate the weekly wage of a worker'''

print("To calculate the weekly wage of a worker:")
hours = float(input("Enter the no. of hours worked: "))
rate = float(input("Enter the hourly rate: "))

if hours <= 35:
	wage = hours * rate
elif hours <= 60:
	wage = rate * 35 + 1.5 * rate * (hours-35)
elif hours <= 70:
	wage = rate * 35 + 1.5 * rate * 25 + 2 * rate * (hours - 60)
else:
	wage = rate * 35 + 1.5 * rate * 25 + 2 * rate * 10
	
#wage = hours * rate if hours <= 35 else (rate * 35 + 1.5 * rate * (hours-35) if hours <= 60 else (rate * 35 + 1.5 * rate * (hours-35) + 2 * rate * (hours - 60) if hours <= 70 else rate * 35 + 1.5 * rate * (hours - 35) + 2 * rate * 10))

print("\nHOURS WORKED\t\t:\t", hours,
	"\nRATE\t\t:\tRs",rate,
	"\nWEEKLY WAGE\t\t:\tRs ",round(wage,2))
