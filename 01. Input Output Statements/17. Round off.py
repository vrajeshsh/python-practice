'''Round off a real number to specific decimal place as specified by user'''

print("To round off a real number to specific decimal place: ")
num = float(input("Enter a fractional number: "))
dec = int(input("Enter number of places to round: "))

#integral = int(num*(10**(dec+1)))/(10**(dec+1))
integral = int(((10**dec)*num)+0.5)/(10**dec)

print("\nIntegral Part: ",integral)
