import os
os.system("cls")

def isPrime(num):
    if num<2:
        return False
    for i in range(2, int(num**.5)+1):
        if num%i==0:
            return False
    return True

pairs=""
num = int(input("Enter a number to prove Goldbach's Conjecture: "))

if num>2 and num%2==0:
    print("\nGoldbach Prime Pairs for",num,"are:")
    for i in range(2, num//2+1):
        if isPrime(i) and isPrime(num-i):
            print(num,"=",i," + ",(num-i))
    print()
else:
    print("\nPlease enter an even number greater than 2 to prove the Conjecture!\n")
