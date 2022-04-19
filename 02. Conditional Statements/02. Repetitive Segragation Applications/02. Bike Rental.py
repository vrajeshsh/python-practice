'''To calculate bike fare based on number of days of rent'''

print("To calculate bike fare based on number of days of rent:")
bike_num = input("Enter Mobike number: ")
phone = input("Enter Mobile number: ")
days = int(input("Enter number of days: "))

charge = 500 * days if days <= 5 else (2500 + 400 * (days - 5) if days <= 10 else 500 * 5 + 400 * 5 + 200 * (days - 10))

print("\nBIKE NO.\t\t:\t", bike_num,
	"\nPHONE NO.\t\t:\t", phone,
	"\nNO. OF DAYS\t\t:\t",days,
	"\nCHARGES\t\t\t:\tRs ",charge)
