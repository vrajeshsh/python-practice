import os
from subprocess import HIGH_PRIORITY_CLASS
os.system("cls")

facs = ""
def sumOfFactors(num):
    ssum=0
    for i in range(1, num//2+1):
        if num%i==0:
            ssum+=i
    return ssum

print("To find Perfect numbers:")
limit = int(input("Enter the limit: "))

for i in range(1, limit+1):
    if sumOfFactors(i)==i:
        facs+= str(i) if facs=="" else ", "+str(i)

if facs=="":
    print("\nNo Perfect number found till ", limit, "\n")
else:
    print("\nPerfect numbers between 1 -",limit," are\n",
        facs,"\n",sep='')
