import os
os.system("cls")

def getSorted(num, order):
    sortedNum, pwr = 0, 0
    for i in range(0, 10):
        temp = num
        while temp > 0:
            dig = temp%10
            temp//=10
            if dig==i:
                sortedNum= sortedNum*10+dig if order==1 else sortedNum+dig*(10**pwr)
                pwr+= 1
    return sortedNum

def formIntegers(num):
    primeDigNum, evenDigNum = 0, 0
    while num > 0:
        dig = num%10
        if dig%2==0:
            evenDigNum = evenDigNum*10+dig
        if dig==2 or dig==3 or dig==5 or dig==7:
            primeDigNum = primeDigNum*10+dig
        num//=10
    if primeDigNum==0:
        print("\nNo Prime digit found in the integer!")
    else:
        print("\nHighest Prime-digited integer: ", getSorted(primeDigNum, 2))
    if evenDigNum==0:
        print("No even digit found in the integer!\n")
    else:
        print("Lowest even-digit integer: ", getSorted(evenDigNum,1),"\n")

num = int(input("Enter an integer to form even and prime digit numbers from its digits: "))
formIntegers(num)
