import os
os.system("cls")

print("To calculate the sum of odd and product of even numbers:")

evensum, oddprod, i = 0, 1, 0

print("\nGo on entering numbers below. Enter 0 to stop.")
while True:
    i+= 1
    print("Enter number", i,": ", end='')
    num = float(input())
    if num == 0:
        break
    if num%2==0:
        evensum+= num
    else:
        oddprod*= num

print("\nSum of even numbers: ",evensum,
    "\nProduct of odd numbers: ",oddprod,"\n", sep='')