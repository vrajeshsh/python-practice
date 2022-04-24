'''Calculate theHCF of two integers'''

print("To calculate the HCF of two integers:")
num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))

for i in range(1, min(num1, num2)):
	if num1%i==0 and num2%i==0:
		hcf=i

print("\nHighest Common Factor of ",num1,"and",num2,": ",hcf)