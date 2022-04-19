'''To Interchange values of two variables USING 2 variables'''

print("To Interchange values of two variables without using any variable:")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("\nValues before swap: ", num1, num2)

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print("\nValues after swap: ",num1, num2)