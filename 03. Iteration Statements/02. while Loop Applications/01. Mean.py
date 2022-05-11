import os
os.system("cls")

print("To calculate the mean of digits of an integer:")
num = int(input("Enter an integer: "))

temp, ssum, count = num,0,0
while(temp>0):
    ssum+= temp%10
    temp//=10
    count+=1
mean = ssum/(1 if count==0 else count)

print("\nThe Mean of the digits of",num,":",mean, "\n")