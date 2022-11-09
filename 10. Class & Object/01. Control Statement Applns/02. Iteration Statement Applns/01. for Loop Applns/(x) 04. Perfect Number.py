import os
os.system("cls")

class PerfectNumbers():
    def __init__(self, lim):
        self.lim = lim

    def sumOfFactors(self, n):
        ssum = 0
        for i in range (1, n//2+1):
            if n%i==0:
                ssum+=i
        return ssum

    def isPerfect(self, n):
        return self.sumOfFactors(n)==n
    ''' 
    Present the output of theis program as per requirement: e.g.
    Perfect Numbers below 30 are:
    6 = 1+2+3
    28 = 1+2+4+7+14

    (Note: Get this done using just that same loop used in the method.)
    '''
    def perfectNosBelow(self):
        print("\nPerfect numbers between 1 and ",self.lim,"are:")
        for i in range(1, self.lim+1):
            if self.isPerfect(i):
                print(i,", ", end="")

print("To find Perfect Numbers upto a given limit: ")
lim = int(input("Enter the limit: "))

obj = PerfectNumbers(lim)
obj.perfectNosBelow()