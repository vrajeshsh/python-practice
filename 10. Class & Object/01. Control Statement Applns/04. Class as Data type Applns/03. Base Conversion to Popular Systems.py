import os
os.system("cls")

class Number():
    def __init__(self, n, b):
        self.num = n
        self.base = b
    
    def isCompatible(self): 
        if self.base != 2 and self.base !=8 and self.base != 10:
            return False
        temp = self.num
        while temp > 0:
            dig= temp%10
            temp//=10
            if dig >= self.base:
                return False
        return True

    def display(self):
        baseName = "Binary" if self.base==2 else "Octal" if self.base==8 else "Decimal"
        print(self.num," (",baseName,")", sep='', end= '')
    
    def toDenary(self): 
        temp, i, dec = self.num, 0, 0
        while temp>0:
            dec+= (temp%10)*pow(self.base, i)
            i+=1
            temp//=10
        return Number(dec, 10)
      
    def toBinary(self):
        binNum, temp, i = 0, self.toDenary().num, 0
        while temp>0:
            binNum+= (temp%2)*pow(10, i)
            i+= 1
            temp//=2
        return Number(binNum, 2)
    
    def toOctal(self):
        octNum, temp, i= 0, self.toDenary().num, 0
        while temp>0:
            octNum+= temp%8*pow(10, i)
            i+=1
            temp//=8
        return Number(octNum, 8)

print("To check whether an integer is compatible and convert it to other popular bases:")
num = int(input("Enter the number: "))
base = int(input("Enter the base: "))

number= Number(num, base)
if number.isCompatible():
    number.toBinary().display()
    print( " = ", end= '', sep= '')
    number.toOctal().display()
    print(" = ", sep= '', end= '')
    number.toDenary().display()
    print()
else:
    print("\nThe number \'", num,"\' is INCOMPATIBLE with the base \'", base,"\'!\n", sep='')