import os
os.system("cls")

class ExpSeries():
    def __init__(self):
        self.lim1= self.lim2 = self.step = 0

    def degToRad(self, deg):
        return (deg/180)*(22/7)

    def expVal(self, x, n):
        ssum = 0
        for i in range(n+1):
            fact = 1
            for j in range(1, i+1):
                fact*= j
            ssum+= x**i/fact
        return ssum

    def accept(self):
        self.lim1 = int(input("Enter the start limit: "))
        self.lim2 = int(input("Enter the ending limit: "))
        self.step = int(input("Enter the step: "))

    def showExpTable(self):
        print("\nDegrees\t\tExp Values")
        for i in range(self.lim1, self.lim2+1, self.step):
            print(i, "\t\t",round(self.expVal(self.degToRad(i), 9), 3)) # 9 is the optimum no. of terms

print("To calculate the Exponential Values for a range of degrees: ")
obj = ExpSeries()
obj.accept()
obj.showExpTable()