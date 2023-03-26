import os
os.system("cls")

class Number():

    def __init__(self, nu, ba):
        self.num = nu
        self.base = ba
    ''' Below method's code needs to FIXED under the guidelines of number & base compatibility concepts'''
    def isCompatible(self):
        if not 2<=self.base<=36:
            return False
        for i in self.num:
            if i.isnumeric() and int(i)>self.base or i.isalpha() and ord(i)-55>self.base:
                return False
        return True
            
    def display(self):
        print(self.num, " (Base ", self.base,") ", sep='', end='')

    def toBase10(self):
        dec, temp, cnt = 0, self.num, 0
        for i in range(len(temp)-1, -1, -1):
            if temp[i].isnumeric():
                dec+=int(temp[i])*pow(self.base, cnt)
            else:
                dec+=ord(temp[i])-55*pow(self.base, cnt)
            cnt+=1
        return Number(dec, 10)

        
    def toBaseX(self, baseX):
        pass

    def showConversion(self, baseX):
        if self.isCompatible():
            print()
            self.display()
            print(" = ", end='', sep='')
            self.toBaseX(baseX).display()
        else:
            print("\nThe number \'",num, "\' is found incompatible with the base \'", base,"\'!\n", sep='')

print("To convert a number from it's given base to any other base [2 - 36]:")
num = input("Enter the number: ")
base = int(input("Enter the base: "))
baseX = int(input("\nEnter the base to be converted to: "))

number = Number(num, base)
number.toBase10().display()
# number.showConversion(baseX)