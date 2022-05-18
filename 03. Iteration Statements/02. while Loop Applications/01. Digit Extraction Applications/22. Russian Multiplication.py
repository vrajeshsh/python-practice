import os
os.system("cls")

print("To multiply two numbers using russian multiplication:")
num1 = int(input("Enter the first integer: "))
num2= int(input("Enter the second integer: "))

mult, ssum="", 0

while(num1>0):
    mult+=str(num1)+"\t\t"+str(num2)+"\n"
    if num1%2==1:
        ssum+=num2
    num2*=2
    num1//=2

print("\nDIVIDED BY 2\tMULTIPLIED BY 2\n",mult,"Product:\t",ssum, '\n', sep="")