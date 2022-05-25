import os
os.system("cls")

def isPrime(num):
    if num<2:
        return False
    for i in range(2, int(num**.5)+1):
        if num%i==0:
            return False
    return True

twins=""
begin = start = int(input("Enter the starting limit: "))
end = int(input("Enter the ending limit: "))

if start<3:
    start=3
if start%2==0:
    start+=1

for i in range(start, end+1, 2):
    if isPrime(i) and isPrime(i-2) and start+2<=i<=end:
        twins+="\n("+str(i-2)+", "+str(i)+")"

if twins=="":
    print("\nNo TWIN Primes found between",begin,"and",end, "\n")
else:
    print("\nTwin Primes found between",begin,"and",end,"are:",twins,"\n")
