'''To calculate new annual salary based on performance rating'''

print("To calculate new annual salary based on performance rating:")
name = input("Name of employee: ")
id_num = int(input("ID number: "))
rating = int(input("Performance Rating: "))
curr_sal = float(input("Current annual salary: Rs "))

if rating == 1:
	interpret = "Excellent"
	hike = 0.1 * curr_sal
elif rating == 2:
	interpret = "Good"
	hike = 0.075 * curr_sal
elif rating == 3:
	interpret = "Average"
	hike = 0.05 * curr_sal
elif rating == 4:
	interpret = "Below Average"
	hike = 0.025 * curr_sal
elif rating == 5:
	interpret = "Poor"
	hike = 0
else:
	interpret = "Not Applicable"
	hike = 0
	print("\nPlease enter a rating between 1(best) and 5(worst)!")

print("\n",name,"'s (ID: ",id_num,") Performance Review:",
	"\n\nPerformance Rating\t:\t",rating,
	"\nInterpretation\t\t:\t",interpret,
	"\nRaise in salary\t\t:\tRs ",hike,
	"\nNew raised salary\t:\tRs ", (curr_sal+hike),sep='')
