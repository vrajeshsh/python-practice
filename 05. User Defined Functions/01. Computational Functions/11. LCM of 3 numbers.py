import os
os.system("cls")

def LcmOf(num1, num2):
    limit = num1*num2
    for i in range(1, limit):
        if i%num1 == 0 and i%num2==0:
            lcm = i
            break
    return lcm

print("To calculate the LCM of 3 numbers:")
num1 = int(input("Enter number #1: "))
num2 = int(input("Enter number #2: "))
num3 = int(input("Enter number #3: "))

lcm = LcmOf(num1,LcmOf(num2, num3))

print("\nLCM of ",num1,", ",num2," and ",num3," : ",lcm,"\n", sep='')