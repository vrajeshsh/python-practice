import os
os.system("cls")

def isPrime(num):
    if num<2:
        return False
    for i in range(2, int(num**.5)+1):
        if num%i==0:
            return False
    return True

def isQualifying(num):
    global facs
    facs= ""
    prod=1
    for i in range(2, num//2+1):
        if num%i==0 and isPrime(i):
            prod*=i
            facs+=str(i) if facs=="" else " x "+str(i)
    return prod==num

facs=""
num = int(input("Enter the limit for generating the numbers: "))

print("\nThe numbers equal to the product of their prime factors from 1 till",
        num,"are:")
for i in range(2, num+1):
    if isQualifying(i):
        print(i, " (",facs,")", sep='')
print()
    