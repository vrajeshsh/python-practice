'''To calculate Years, Months and Days based on number of days'''

print("To calculate Years, Months and Days based on number of days:")
total_days = int(input("Enter the number of days: "))

years = total_days//365
months = (total_days%365)//30
days = (total_days%365)%30

print("\n", total_days," days = ",
	years," year(s) ",months," month(s) and ",days," day(s)")

# Present the output as 1200 days = 1 year(s) 2 month(s) 23 days(s)