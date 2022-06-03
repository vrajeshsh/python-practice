import os
os.system("cls")

def getSorted(num, order):
    srt=""
    for i in range(0, 10):
        temp = num
        while(temp>0):
            dig = temp%10
            if i == dig:
                if order==1:
                    srt+=str(dig)
                else:
                    srt=str(dig)+srt
            temp//=10
    return int(srt)

def formIntegers(num):
    primes, even = 0, 0
    while(num>0):
        dig = num%10
        if dig%2==0:
            even = (even*10)+dig
        if dig==2 or dig==3 or dig==5 or dig==7:
            primes = (primes*10)+dig
        num//=10
    if primes==0:
        print("\nNo Prime digit found in the integer!")
    else:
        print("\nHighest Prime-digited integer: ", getSorted(int(primes), 2))
    if even==0:
        print("No Even digit found in the integer!\n")
    else:
        print("Lowest even-digited integer: ", getSorted(int(even),1),"\n")


num = int(input("Enter an integer: "))
formIntegers(num)

# i dont know how to sort integer numbers
#can you please give a hint
'''
work as per the hint and and i will check this tomorrow

set a loop to range from 0 to 9
inside extract each digit
when the digit equals the outer loop value build a new number.
'''
