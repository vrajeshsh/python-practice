'''Conversion chart for centigrade to Fahrenheit temperature'''

print("Conversion chart for centigrade to Fahrenheit temperature:")

temp=""

print("\nTemperature conversion table:",
	"\nCentigrade\t\tFahrenheit")
for c in range(0,101,5):
	f = (9/5) * c + 32
	print(c,"\t\t\t\t", f)
