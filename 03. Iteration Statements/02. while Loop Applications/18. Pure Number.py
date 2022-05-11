import os
os.system("cls")

print("To check if a given number is a Pure number or not:")
num = int(input("Enter the integer: "))

temp, count, revnum = num, 0, 0
while(temp > 0):
    dig = temp%10
    if dig==4 or dig==5:
        revnum = revnum*10+dig
    else:
        break
    count+=1
    temp//=10

print("\nThe integer ",num," is ",
    "" if(revnum==num and count%2==0) else "NOT ", 
    "Pure\n",sep='')
