import os
os.system("cls")

print("To find the ratio of evencnt to oddcnt numbers:")
i, evencnt, oddcnt = 0, 0, 0

print("\nGo on entering numbers below. Enter a negative number to STOP.")

while True:
    i+= 1
    print("Enter number", i,": ", end='')
    num = float(input())
    if num<0:
        break
    if num%2==0:
        evencnt+= 1
    else:
        oddcnt+= 1

# Reducing the two counters below to print their ratio:
i= 2
while i<evencnt and i<oddcnt:       # loop running till the lesser number here
    if evencnt%i==0 and oddcnt%i==0:
        evencnt//= i
        oddcnt//=i
        i-=1
    i+= 1

print("\nThe ratio of Even : Odd = ", evencnt," : ", oddcnt,"\n",sep='')
