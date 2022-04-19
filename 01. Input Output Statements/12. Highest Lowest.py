'''To calculate highest and lowest integers of a 3-digit integer'''

print("To find the  highest and lowest digits of a 3-digit integer:")
num = int(input("Enter a 3-digit integer: "))

rem1 = num%10
rem2 = (num//10)%10
rem3 = num//100

max = max(rem1,rem2,rem3)
min = min(rem1,rem2,rem3)

print("\nMaximum: ",max,
	"\nMinimum: ",min)
