import os
os.system("cls")

print("To check if a given number is Niven or not:")
num = int(input("Enter the integer: "))

temp, ssum = num, 0

while(temp > 0):
    dig = temp%10
    ssum+=dig
    temp//=10

if num%ssum==0:
    print("\n",num,"is a Niven number\n")
else:
    print("\n",num,"is not a Niven number\n")
