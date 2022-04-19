'''To accept 3 numbers and arrange in ascending order'''

print("To accept 3 numbers and arrange in ascending order:")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

maxi = max(num1,num2,num3)
mini = min(num1,num2,num3)

if num1 <= num2 <= num3 or num3 <= num2 <= num1:
	mid = num2
elif num1 <= num3 <= num2 or num2 <= num3 <= num1:
	mid = num3
else:
	mid = num1

print("\nThe 3 numbers arranged in ascending order:\n",mini,mid,maxi)
