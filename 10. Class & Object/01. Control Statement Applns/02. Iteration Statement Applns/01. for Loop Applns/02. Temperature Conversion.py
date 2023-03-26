import os
os.system("cls")

class TempConversion():
    def __init__(self, t1, t2, st, sc):
        self.t1 = t1
        self.t2 = t2
        self.st = st
        self.sc = sc

    def toCelcius(self, temp):
        if self.sc.lower()=="c":
            return temp
        elif self.sc.lower()=="f":
            return round((temp - 32)* 5 / 9, 3)
        else:
            return temp - 273

    def toFahrenheit(self, temp):
        if self.sc.lower()=="c":
            return  round((9/5)*temp+32, 3)
        elif self.sc.lower()=="f":
            return temp
        else:
            return (9/5)*(temp - 273)+32

    def toKelvin(self, temp):
        if self.sc.lower()=="c":
            return temp + 273
        elif self.sc.lower()=="f":
            return round((temp - 32) * (5/9), 3)+273
        else:
            return temp

    def showConversion(self):
        print("\nCENTIGRADE\tFAHRENHEIT\tABSOLUTE")
        for i in range(self.t1, self.t2+1, self.st):
            print(self.toCelcius(i),"\t\t",self.toFahrenheit(i),"\t\t", self.toKelvin(i),sep='')
        print()

print("To convert temperatures from one scale to another scale:")
t1 = int(input("ENter the start limit: "))
t2 = int(input("Enter the end limit: "))
step = int(input("Enter the step value: "))
scale = input("Enter the scale [C/F/K]: ")

obj = TempConversion(t1, t2, step, scale)
obj.showConversion()