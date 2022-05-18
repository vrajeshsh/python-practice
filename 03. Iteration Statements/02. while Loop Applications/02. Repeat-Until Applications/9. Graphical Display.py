import os
os.system("cls")

print("To graphically display number of even, odd, prime and composite")

i, even, odd, prime, comp = 0, 0, 0, 0, 0

while True:
    i+= 1
    print("Enter integer", i,": ", end='')
    temp = num = int(input())
    if num==0:
        break
    while(temp>0):
        dig = temp%10
        if dig%2==0:
            even+=1
        elif dig%2==1:
            odd+=1
        if dig==2 or dig==3 or dig==5 or dig==7:
            prime+=1
        elif dig==4 or dig==6 or dig==8 or dig==9:
            comp+=1
        temp//=10

print("\nEven\t:\t",even*'##', "\nOdd\t:\t", odd*'##',
"\nPrime\t:\t",prime*'##', "\nComposite:\t", comp*'##',"\n")