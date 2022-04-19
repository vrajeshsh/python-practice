'''To calculate the average and Total of 3 subjects'''

print("To calculate Average and Total marks of 3 subjects:")
mks1 = float(input("Enter marks in 1st subject : "))
mks2 = float(input("Enter marks in 2nd subject : "))
mks3 = float(input("Enter marks in 3rd subject : "))

total = mks1+mks2+mks3
avg = total/3

print("\nThe Total marks in 3 subjects :", total,
	"\nAverage marks: ", round(avg,3))
