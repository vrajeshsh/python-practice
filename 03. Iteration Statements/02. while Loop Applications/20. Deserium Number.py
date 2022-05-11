import os
os.system("cls")

print("To check if a given number is a Deserium number or not:")
num = n = int(input("Enter an integer: "))

ssum, count = 0, 0

while(n > 0):
    count+= 1
    n//= 10
n= num    
while(n > 0):
    dig = n%10
    ssum+= dig** count
    count-= 1
    n//=10

print("\nThe integer ",num," is ",
    "" if(ssum==num) else "NOT ", 
    "Deserium\n",sep='')
