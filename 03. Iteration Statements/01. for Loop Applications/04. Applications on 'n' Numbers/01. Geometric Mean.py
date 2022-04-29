'''To calculate the geometric mean of n numbers'''

print("To calculate the geometric mean of n numbers:")
n = int(input("Enter number of numbers: "))

prod=1
print()
for i in range(1,n+1):
    print("Enter Number #",i,": ", sep='', end='')
    num = float(input())
    prod*=num
    
gm = prod**(1/n)    # GM is calc as the nth root of the product -- SO CARELESS

print("\nThe Geometric Mean of all numbers: ",gm)

# Accepted