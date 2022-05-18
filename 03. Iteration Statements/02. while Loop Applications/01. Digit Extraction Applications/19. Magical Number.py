import os
os.system("cls")

print("To check if a given number is a Magical number or not:")
num = int(input("Enter an integer: "))

temp, ssum = num, 0
while(temp>0 or ssum>9):
    if(temp==0):
        temp = ssum
        ssum = 0
    ssum+=temp%10
    temp//=10
    
print("\nThe integer ",num," is ",
    "" if(ssum==1) else "NOT ", 
    "Magical\n",sep='')
