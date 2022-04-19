'''To find the second highest among 3 numbers'''

print("To find the second highest among 3 numbers:")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

maxi = max(num1,num2,num3)
mini = min(num1,num2,num3)

if mini<=num1<maxi:
	sec = num1
elif mini<=num2<maxi:
	sec = num2
else:
	sec = num3

if num1==num2==num3:
	print("\nAll numbers are equal")
else:
	print("\nSecond highest value among ",num1,", ",num2,", ",num3,": ",sec,sep='')
