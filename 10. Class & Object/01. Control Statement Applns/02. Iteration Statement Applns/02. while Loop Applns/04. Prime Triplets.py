import os
from socket import SIO_RCVALL
import this
from tkinter import W
os.system("cls")

class PrimeTriplets():
    def __init__(self, n):
        self.n = n

    def isPrime(self, n):
        if n<2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n%i==0:
                return False
        return True

    def areAllDigitsPrime(self, n):
        while n>0:
            dig = n%10
            if not (dig==2 or dig==3 or dig==5 or dig==7):
                return False
            n//=10
        return True
    
    def generateTriplets(self):
        #Work WITHOUT string for a change JUST with the isFound boolean variable...
        isFound = False
        for i in range(5, self.n+1):
            if (self.areAllDigitsPrime(i-2) or self.isPrime(i-2)) and \
                (self.areAllDigitsPrime(i-1) or self.isPrime(i-1)) and \
                (self.areAllDigitsPrime(i) or self.isPrime(i)):
                if not isFound:
                    print("\nPrime Triplets till ",self.n," are:")
                isFound = True
                print("(",i-2,", ",i-1,", ",i,")", sep='')

        if not isFound:
            print("\nNo Prime Triplets found in the given range!\n")

# Just print the message 'No such triplets found!'

print("To display Prime Triplets upto a given limit: ")
lim = int(input("Enter the limit: "))

obj = PrimeTriplets(lim)#okay sir actually i was avoiding taking a variable, ill do the full thing now
obj.generateTriplets()
#You are sooooooom  +ve minded!!

#changing sir

#         Go like real-life... 
#         When you tread a path... you go step-by-step... ahead...   
#         this way you move only... You can never reach the destination   
#         any way and come back... Life does not give that chance...
#         We reach our destination right at the end...

#         Just as in real-life... while we tread... we feel 'dara-dara... '
#         'samha samha'.... still alone we move...
#         ... AND when we reach our 'man-pasad' destination...
#         WHAT JOY WE GET?

#         Proceed in programming also JUST THIS WAY... face the difficulties..
#         LIVE and THEN and THERE... complete one... then move on to the next.  

#         ALL GOOD STUDENTS work this way only... INCLUDING your SIO_RCVALL
#          sure sir