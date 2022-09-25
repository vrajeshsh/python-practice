import os
os.system("cls")

def isPrime(n):
    global den
    den+= 1
    return True if n==2 or den>n//2 else False if n<2 or n%den==0 else isPrime(n)

print("To display Prime factors of a given number:")
n = int(input("Enter the number: "))

facs= ""
for i in range(2, n//2+1):
    den = 1
    if n%i==0 and isPrime(i):
        facs+=str(i) if facs=="" else ", "+str(i)

print("\nPrime factors of ",n," are: ","None" if facs=="" else facs,"\n", sep='')

# No one can CHANGE the approach or ATTITUDE of a programmer towards coding... 
# Being able to write short codes is an art... it comes from within...
# Analogically, the joy you get in saving money, is the same joy that programmer enjoys when
# he/she successfully shortens the code... and it's a never ending incessant endeavour...