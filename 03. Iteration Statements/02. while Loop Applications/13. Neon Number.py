import os
os.system("cls")

print("To check if a given number is Niven or not:")
num = int(input("Enter an integer: "))

temp, ssum = num*num, 0
while(temp>0):
    dig = temp%10
    ssum+=dig
    temp//=10

if num==ssum:
    print("\n",num,"is a Neon number\n")
else:
    print("\n",num,"is not a Neon number\n")

