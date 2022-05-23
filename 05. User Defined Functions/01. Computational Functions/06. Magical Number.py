import os
os.system("cls")

def digitSum(num):
    ssum = 0
    while num>0:
        ssum+=num%10
        num//=10
    return ssum

print("To check Magical or not:")
num = int(input("Enter an integer: "))

ssum = 10
while ssum > 9:
    ssum= digitSum(ssum)

print("\nThe number",num,"is", "" if ssum==1 else "NOT",
    "a Magical number.\n")

