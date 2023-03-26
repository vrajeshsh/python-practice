import os
os.system("cls")

class GoldbachConjecture():
    def __init__(self, num):
        self.num = num

    def isValid(self):
        return self.num>2 and self.num%2==0

    def isPrime(self, n):
        if n<2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n%i==0:
                return False
        return True

    def validateConjecture(self):
        facs = ""
        if self.isValid():
            for i in range(1, self.num//2+1):
                if self.isPrime(i) and self.isPrime(self.num-i):
                    facs+= "\n"+str(self.num)+ " = "+str(self.num-i)+ " + " +  str(i)

        if self.isValid() and facs:
            print("\nThe Goldbach Conjectures are: ", facs,"\n", sep='')
        else:
            print("\nGoldbach's Conjecture is not proven for ",self.num,"!\n", sep='')

print("To find the Goldbach's Conjecture for a given number :")
num = int(input("Enter the number: "))

obj = GoldbachConjecture(num)
obj.validateConjecture()