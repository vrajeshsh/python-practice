import os
os.system("cls")

print("To form odd and even digit-numbers from an integer:")
temp = num = int(input("Enter the integer: "))

odd, indx, even, pow = 0, 0, 0, 0
while(temp>0):
    dig=temp%10
    temp//=10
    if dig%2==0:
        even+= dig*10**indx     # number formed through 'forward concatenation' of digits
        indx+= 1
    else:
        odd+= dig*10**pow
        pow+= 1
    
print("\nEven-digit number: ",even,
    "\nOdd-digit number: ",odd,"\n",sep='')

'''
Sample I/O:
Input: 24852725
Output:
Even-digut number: 24822
Odd-dogit number: 575

Hope this helps
yes yes thankyou
'''