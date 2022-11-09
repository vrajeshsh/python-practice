import os
os.system("cls")

class AnyBase():
    def __init__(self, nu, ba):
        self.num = nu
        self.base = ba

    def isCompatible(self):
        if self.base!=2 and self.base!=8 and self.base!=10:
            return False
        temp = self.num
        while temp>0:
            dig = temp%10
            temp//=10
            if dig>=self.base:
                return False
        return True

    def display(self):
        baseName = "Binary" if self.base==2 else "Octal" if self.base==8 else "Decimal"
        print(self.num," (",baseName,")", sep='', end='')

    def toBase10(self):
        temp, i, dec = self.num, 0, 0
        while temp>0:
            dec+= temp%10*pow(self.base, i)
            i+=1
            temp//=10
        return AnyBase(dec, 10)

    def toBaseX(self, baseX):
        num, temp, i = 0, self.toBase10().num, 0
        while temp>0:
            num+= (temp%baseX)*pow(10, i)
            i+= 1
            temp//=baseX
        return AnyBase(num, baseX)
    
    def showConversion(self, baseX):
        if self.isCompatible():
            print()
            self.display()
            print(" = ", end='', sep='')
            self.toBaseX(baseX).display()
        else:
            print("\nIncompatible\n")

print("To convert number in a given base to any other base:")
num = int(input("Enter the number: "))
base = int(input("Enter the base: "))
baseX = int(input("Enter the base to be converted to: "))

number = AnyBase(num, base)
number.showConversion(baseX)

''' Kindly complete the other programs too. Will check all these on Friday. '''