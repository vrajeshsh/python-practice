import numbers
import os
os.system("cls")

print("To form new numbers from digits:")
num = int(input("Enter the integer: "))

newStr=""

for i in range(10):
    temp = num
    count = 0
    while(temp>0):
        dig = temp%10
        if dig== i:
            count+= 1
        temp//=10
    if count>0:
        newStr+= str(i)+"\t\t"+str(count)+"\n"

print("\nDIGIT\tFREQUENCY\n",newStr, sep='')

