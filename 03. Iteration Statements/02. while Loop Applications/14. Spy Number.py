import os
os.system("cls")

print("To check if a given number is Niven or not:")
num = int(input("Enter an integer: "))

temp, ssum, prod = num, 0, 1
while(temp>0):
    dig = temp%10
    ssum+=dig
    prod*=dig
    temp//=10

if prod==ssum:
    print("\n",num,"is a Spy number\n")
else:
    print("\n",num,"is not a Spy number\n")