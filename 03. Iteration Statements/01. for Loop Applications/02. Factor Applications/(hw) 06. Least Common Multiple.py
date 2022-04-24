'''Calculate the LCM of two integers'''

print("To calculate the LCM of two integers:")
num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))

maxi=max(num1,num2)

for i in range(maxi,num1*num2+1,maxi):
	if i%min(num1,num2)==0:
		lcm = i
		break

print("\nLeast Common Multiple of",num1,"and",num2,": ",lcm)

 #Try to develop a STAND-ALONE version of LCM calcn that does not use the HCF algorithm.0

