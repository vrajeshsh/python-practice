import os
os.system("cls")

def hcfOf(num1, num2):
    limit = min(num1, num2)
    for i in range(1, limit+1):
        if num1%i==0 and num2%i==0:
            hcf = i
    return hcf

print("To calculate the HCF of 3 numbers:")
num1 = int(input("Enter number #1: "))
num2 = int(input("Enter number #2: "))
num3 = int(input("Enter number #3: "))

hcf= hcfOf(num1,hcfOf(num2, num3))

print("\nHCF of ",num1,", ",num2," and ",num3," : ", hcf, "\n", sep='')