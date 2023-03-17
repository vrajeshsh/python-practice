import os
os.system("cls")

class Fraction():
    def __init__(self, num, den):
        self.num = num
        self.den = den
    ''' More attributes of printing fractions STILL LEFT to be completed for the below method. '''
    def display(self):
        if self.den==0:
            print("\nInfinity")
        elif self.den==1 or self.num==0:
            print(self.num, sep='')
        elif self.den<0:
            print("-",self.num,"/",abs(self.den),sep='')
        else:
            print(self.num,"/",self.den, sep='')

    def reduce(self):
        i = 2
        while i<abs(self.num)+1 and i<abs(self.den)+1:
            if self.num%i==0 and self.den%i==0:
                self.num//=i
                self.den//=i
                i-=1
            i+=1
        
    def addTo(self, frac):
        sumFrac = Fraction(self.num*frac.den + frac.num*self.den, self.den*frac.den)
        sumFrac.reduce()
        return sumFrac

    def subFrom(self, frac):
        diffFrac = Fraction(self.num*frac.den - frac.num*self.den, self.den*frac.den)
        diffFrac.reduce()
        return diffFrac

    def mulWith(self, frac):
        prodFrac = Fraction(self.num*frac.num, self.den*frac.den)
        prodFrac.reduce()
        return prodFrac

    def divBy(self, frac):
        divFrac = Fraction(self.num*frac.den, self.den*frac.num)
        divFrac.reduce()
        return divFrac

print("To perform simple arithmatical operations on fractions:",
    "\nEnter details for first fraction:")
num1 = int(input("Enter numerator: "))
den1 = int(input("Enter denominator: "))
print("Enter details for the second fraction: ")
num2 = int(input("Enter numerator: "))
den2 = int(input("Enter denominator: "))

frac1, frac2 = Fraction(num1, den1), Fraction(num2, den2)

print("\nThe first Fraction: ", end='')
frac1.display()
print("The second fraction: ", end='')
frac2.display()
print("\nSum: ", end='')
frac1.addTo(frac2).display()
print("Difference: ", end='')
frac1.subFrom(frac2).display()
print("Product: ", end='')
frac1.mulWith(frac2).display()
print("Quotient: ", end='')
frac1.divBy(frac2).display()
print()