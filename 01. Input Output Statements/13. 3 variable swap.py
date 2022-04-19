'''To Interchange values of two variables USING 3rd variable'''

print("To interchange the values of two variables by using 3rd variable:")
num1 = float(input("Enter the  first number: "))
num2 = float(input("Enter the second number: "))

print("\nValues before swap: ", num1, num2)

temp = num1
num1 = num2
num2 = temp

print("\nValues after swap: ",num1, num2)