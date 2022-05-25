import os
os.system("cls")

def isPrime(num):
    if num<2:
        return False
    for i in range(2, int(num**.5)+1):
        if num%i==0:
            return False
    return True

count, num = 1, 2

n = int(input("Enter the value of 'n' to find the nth Prime: "))
while count < n:
    num+= 1
    if isPrime(num):
        count+=1
d= n%10
sufx= "st" if d==1 and n!= 11 else "nd" if d==2 and n!=12 \
 else "rd" if d==3 and n!= 13 else "th" 
print("\nThe ",count,sufx, " prime number is ",num,"\n",sep='')
