import os
from pickle import FALSE
os.system("cls")

class PrimeTriplets():
    def __init__(self, n):
        self.n = n

    def areAllFactorsPrime(self, n):
        if n<2:
            return False
        for i in range(2, n//2+1):
            if n%i==0:
                for j in range(2, int(i**0.5)+1):
                    if i%j==0:
                        return False
            return True
            
    def generateTriplets(self):
        for i in range(5, self.n+1,3):
            if self.areAllFactorsPrime(i-2) and self.areAllFactorsPrime(i-1) and self.areAllFactorsPrime(i):
                print("(",i-2," , ",i-1," , ",i,"), ", sep='')

print("To find Prime Triplets upto a given limit: ")
lim = int(input("Enter the limit: "))

obj = PrimeTriplets(lim)
obj.generateTriplets()
print()

#sir only prime triplets is not fully done yet, other two are done