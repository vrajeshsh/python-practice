from msilib import knownbits
import os
os.system("cls")

print("To form new numbers from a given integer:")
temp = num = int(input("Enter the integer: "))

newNum, pow, ssum, numStr = 0, 1, 0, "" 

while(temp>0):
    dig = temp%10
    newNum+=dig*pow
    ssum+=newNum
    numStr+=str(newNum) if numStr=="" else ", "+str(newNum)
    pow*=10
    temp//=10

print("\nNew numbers:",numStr,"\nSum:",ssum,"\n")