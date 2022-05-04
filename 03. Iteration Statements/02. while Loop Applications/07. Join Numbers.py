import os
os.system("cls")

print("To join two integers digitally:")
num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))

temp, count = num2, 0

while(temp>0):
    dig=temp%10
    count+=1
    temp//=10
dig_join = num1*(10**count)+num2

print("\nDigital join of",num1,"and",num2,"is",dig_join, "\n")