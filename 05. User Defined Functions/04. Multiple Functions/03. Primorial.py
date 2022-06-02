import os
os.system("cls")

def isPrime(num):
    if num<2:
        return False
    for i in range(2, int(num**.5)+1):
        if num%i==0:
            return False
    return True

def primorial(num):
    global facs
    facs= ""
    prod = 1
    for i in range(2, num+1):
        if isPrime(i):
            facs+=str(i) if facs=="" else " x "+str(i)
            prod*=i
    return prod
    
num = int(input("Enter an integer to calculate its Primorial: "))
primo = primorial(num)
if facs=="":
    print("\nPlease enter a number greater than 1!\n")
else:
    print("\n",num,"# = ",facs," = ",primo,"\n", sep='')
