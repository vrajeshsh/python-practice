import os
os.system("cls")
'''
I AM CODING IN 2022 FOR US IT JOBS.
'''
class AmicableNumber():
    def __init__(self):
        self.lim1 = self.lim2 = 0

    def input(self):
        self.lim1 = int(input("Enter the starting limit: "))
        self.lim2 = int(input("Enter the end limit: "))
    
    def sumOfAliquots(self, n):
        ssum = 0
        for i in range(1, n//2+1):
            if n%i==0:
                ssum+=i
        return ssum

    def areAmicable(self, num1, num2):
        return (self.sumOfAliquots(num1)==num2 and self.sumOfAliquots(num2)==num1)
    '''
    Kindly fix the below code so as to produce the 'exact output' as expected by the program using
    the SAME ONE loop as used below.

    SAMPLE INPUT:
    1, 1000
    SAMPLE OUTPUT:
    THE AMICABLE NUMBERS BETWEEN 1 AND 1000 ARE:
    PAIR #1.
    220 (1+2+4+5+10+11+20+22+44+55+110 = 284)
    284 (1+2+4+71+142 = 220)
    '''
    def showAmicableNos(self):
        isFound, lim = False, self.lim1 
        while lim <= self.lim2:
            aliSum = self.sumOfAliquots(lim)
            if self.areAmicable(lim, aliSum) and lim!=aliSum:
                if not isFound:
                    print("\nAmicable numbers between ",self.lim1," and ", self.lim2,": ",sep='')
                isFound = True
                print("(",lim,", ",aliSum,")", sep='')
                lim = aliSum+1
            else:
                lim+=1
        if not isFound:
            print("\nNO Amicable numbers present in the given range!")

print("To display Amicable no.s upto a given limit: ")

obj = AmicableNumber()
obj.input()
obj.showAmicableNos()
print()