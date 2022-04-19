'''To calculate Integral and Fractional portions of a real number'''

print("Calculate Integral and Fractional portions of a real number:")
real_num = float(input("Enter any real (fractional) number: "))

int_part= int(real_num)
frac_part= real_num - int_part

print("\nIntegral Part: ", int_part,
	"\nFractional Part: ", round(frac_part, 8))