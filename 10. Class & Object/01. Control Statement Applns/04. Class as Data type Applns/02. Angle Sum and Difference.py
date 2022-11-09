import os
os.system("cls")

class Angle():
    def __init__(self, dg, mn):
        self.deg = dg
        self.mn = mn

    def showAngle(self):
        print(self.deg,chr(176)," ",self.mn,"'", sep='')

    def angleToMinutes(self):
        return self.deg*60+self.mn

    def minsToAngle(self, mins):
        self.deg = mins//60
        self.mn = mins%60
    
    def add(self, ang1, ang2):
        self.minsToAngle(ang1.angleToMinutes() + ang2.angleToMinutes())
    
    def getDifference(self, ang):
        difAngle = Angle(0, 0)
        difAngle.minsToAngle(abs(self.angleToMinutes() - ang.angleToMinutes()))
        return difAngle

print("To display the addition and subtraction of two angles:",
    "\nEnter details for the first angle:")
deg1 = int(input("Enter degrees: "))
min1 = int(input("Enter minutes: "))
print("\nEnter details for the second angle:")
deg2 = int(input("Enter degrees: "))
min2 = int(input("Enter minutes: "))

ang1, ang2, sumAngle = Angle(deg1, min1), Angle(deg2, min2), Angle(0, 0)
difAngle = ang1.getDifference(ang2)
sumAngle.add(ang1, ang2)

print("\nFirst angle:")
ang1.showAngle()
print("Second angle:")
ang2.showAngle()
print("\nSummation Angle:")
sumAngle.showAngle()
print("Difference Angle:")
difAngle.showAngle()
print()