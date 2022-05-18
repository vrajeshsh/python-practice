print("To show the first and last digits of an integer:")
num = int(input("Enter an integer: "))

temp, first, last = num, 0, 0
while(temp>0):
    first = temp%10
    temp//=10
last= num%10

print("\nFirst digit:",first,
    "\nLast digit:",last)
