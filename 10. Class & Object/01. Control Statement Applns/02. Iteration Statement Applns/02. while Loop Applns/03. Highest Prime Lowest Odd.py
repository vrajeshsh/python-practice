from concurrent.futures.process import _WorkItem
import os
os.system("cls")

# Caution: I AM CODING IN 2022! 

class Number():
    def __init__(self, num):
        self.num = num

    def isPrimeDig(self, dig):
        return dig==2 or dig==3 or dig==5 or dig==7
    '''
    Reduce the code length of the below method to just ONE BLOCK using two loops
    '''
    def arrangeDigits(self, num, order):
        sortedNum = 0
        if order==1:
            for i in range(10):
                temp = num
                while temp>0:
                    dig = temp%10
                    if i==dig:
                        sortedNum=(sortedNum*10)+dig
                    
                    temp//=10
        else:  
            for i in range(9,0,-1):
                temp = num
                while temp>0:
                    dig = temp%10
                    if i==dig:
                        sortedNum=(sortedNum*10)+dig
                    temp//=10
        return sortedNum
    ''' 
    Remove the loops used quite UNNECESSARILY in the below METHODS by applying some innovation.
    '''
    def maxPrimeDigitedNum(self):
        temp, maxPrime = self.arrangeDigits(self.num,1), 0
        while temp>0:
            dig=temp%10
            if self.isPrimeDig(dig):
                maxPrime = (maxPrime*10)+dig
            temp//=10
        print("\nThe maximum prime digited number: ",maxPrime,sep='')

    # You like Loop after loop after loop? Long long code blocks!!! 
    # No sir but in arrange func i tried the short way and failed so i just copy pasted the whole thing

    def minOddDigitedNum(self):
        temp, minOdd = self.arrangeDigits(self.num,2), 0
        while temp>0:
            dig=temp%10
            if dig%2==1:
                minOdd = (minOdd*10)+dig
            temp//=10
        print("\nThe minimum odd digited number: ",minOdd,sep='')
        

print("To find the highest prime and lowest odd digits in a given number:")
num = int(input("Enter a number: "))

obj = Number(num)
obj.maxPrimeDigitedNum()
obj.minOddDigitedNum()
print()
