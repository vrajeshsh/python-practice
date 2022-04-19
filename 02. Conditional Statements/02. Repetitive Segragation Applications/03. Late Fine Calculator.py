'''To calculate late fine based on number of days late and type of book'''

print("To calculate late fine based on no. of days late and type of book")
name = input("Enter name of student: ")
days_late = int(input("Enter no. of days late: "))
book_type = input("Enter type of book [T/G]:").upper()

if days_late <= 10:
	charge = 3.5 * days_late if book_type=='T' else 5 * days_late
elif days_late <= 15:
	charge = 3.5 * 10 + 5.5 * (days_late - 10) if book_type=='T' else 5 * 10 + 7.5 * (days_late - 10)
elif days_late <= 30:
	charge = 3.5 * 10 + 5.5 * 5 + 7 * (days_late - 15) if book_type=='T' else 5 * 10 + 7.5 * 5 + 10 * (days_late - 15)
else:
	charge = 3.5 * 10 + 5.5 * 5 + 7 * 15 + 10 * (days_late - 30) if book_type=='T'  else 5 * 10 + 7.5 * 5 + 10 * 15 + 15 * (days_late - 30)

print("\nNAME\t\t\t:\t",name,
	"\nDAYS LATE\t\t:\t", days_late,
	"\nBOOK TYPE\t\t:\t",book_type,
	"\nLATE FINE\t\t:\tRs ",charge)
