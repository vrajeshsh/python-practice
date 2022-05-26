import os, math
os.system("cls")

def isTechNumber(num):
    count = int(math.log10(num))+1      #calculating no. of digits in 'num'
    first = num//(10**(count/2))
    last = num%(10**(count/2))
    return (first+last)**2==num

n = int(input("Enter 'n' to find all 'n' digit tech numbers: "))
start, end, tech = 10**(n-1), 10**(n), ""

for i in range(start, end):
    if isTechNumber(i):
        tech+= str(i) if tech=="" else ", "+str(i)

if n%2==0:
    print("\nAll Tech numbers from ",start," to ",(end-1),":\n",tech,"\n",sep='')
else:
    print("\nNo Tech numbers exist in given the range!\n")
 