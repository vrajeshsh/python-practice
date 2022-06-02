import os
os.system("cls")

def isPrime(num):
    if num<2:
        return False
    for i in range(2, int(num**.5)+1):
        if num%i==0:
            return False
    return True

def areAllDigitsPrime(num):
    while num>0:
        if not isPrime(num%10):
            return False
        num//=10
    return True

trip=""
end = int(input("Enter ending limit to check for Triplets: "))

for i in range(3, end+1):
    if (isPrime(i-2) or areAllDigitsPrime(i-2)) and \
       (isPrime(i-1) or areAllDigitsPrime(i-1)) and \
       (isPrime(i) or areAllDigitsPrime(i)):
        trip+="("+str(i-2)+","+str(i-1)+","+str(i)+")\n"

if trip=="":
    print("\nNo Triplets exist in the given range!\n")
else:
    print("\nTriplets from 1 to ",end,":\n",trip, sep='')
