import os
os.system("cls")

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact*=i
    return fact

print("To find the summation of the factorial series:")
x = int(input("Enter value of x: "))
lim = int(input("Enter limit: "))

j, series, ssum = 10, "", 0

for i in range(lim+1):
    term = factorial(x+i)/j   
    series+= str(round(term, 3)) if i==0 else " + "+str(round(term, 3))
    ssum+= term
    j+=5

print("\nSummation Series:\n",series,
    "\nSum: ",ssum,"\n")
