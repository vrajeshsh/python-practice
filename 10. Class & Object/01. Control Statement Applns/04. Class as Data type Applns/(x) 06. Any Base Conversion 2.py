import os
os.system("cls")

class Number():
    def __init__(self, nu, ba):
        self.num = nu
        self.base = ba
    ''' Below method's code needs to FIXED under the guidelines of number & base compatibility concepts'''
    def isCompatible(self):
        if self.num.isnumeric():
            return int(max(self.num))+1<=self.base
        return ord(max(self.num))-54<=self.base
            
    def display(self):
        print(self.num, " (Base", self.base,") ", sep='', end='')

    def toBase10(self):
        num = self.num
        for i in range(len(num)):
            if num[i].isnum():
                number+=num[i]*pow(i,base)
            else :
                number+=(9 + ord(num[i])) *pow(i,base)
        return num

        
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
number.showConversion(baseX)

# Keep this COMPLETED for tomorrow. Will check in class.