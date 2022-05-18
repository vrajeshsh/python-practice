import os
os.system("cls")

print("To display prime digits of an integer:")
num = int(input("Enter the integer: "))

temp, prime, prime_sum=num, "", 0

while(temp>0):
    dig=temp%10
    if dig==2 or dig==3 or dig==5 or dig==7:
        prime+= str(dig) if prime=="" else ", "+str(dig)
        prime_sum+= dig 
    temp//=10

if prime_sum==0:
    print("\nNo prime digits found in the integer!")
else:
    print("\nPrime digits:",prime,"\nSum:",prime_sum,"\n")


