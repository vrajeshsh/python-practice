import os
os.system("cls")

def isPrime(num):
    if num<2:
        return False
    for i in range(2, num//2+1):
        if num%i==0: 
            return False
    return True

def areAllFactorsPrime(num): 
    if num<2:
        return False
    for i in range(2, num//2+1):
        if num%i==0:
            if not isPrime(i):
                return False
    return True

trip=""
print('To generate triplets that are either Prime or have all factors prime:')
begin = start = int(input("Enter the start limit: "))
end = int(input("Enter the end limit: "))

while start+2<=end:
    if (isPrime(start) or areAllFactorsPrime(start)) and \
       (isPrime(start+1) or areAllFactorsPrime(start+1)) and \
       (isPrime(start+2) or areAllFactorsPrime(start+2)):
        trip+="("+str(start)+","+str(start+1)+","+str(start+2)+")\n"
    start+=1

if trip=="":
    print("\nNo Triplets exist in the given range!\n")
else:
    print("\nTriplets from ",begin," to ",end,":\n",trip,"\n",sep='')