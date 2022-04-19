'''To calculate remainder of two integers'''
print("To find the remainder of the division of two integers:")
num = int(input("Enter numerator: "))
denom = int(input("Enter denominator: "))

rem = num-((num//denom)*denom)

print("\n",num,"%",denom," = ", rem)
