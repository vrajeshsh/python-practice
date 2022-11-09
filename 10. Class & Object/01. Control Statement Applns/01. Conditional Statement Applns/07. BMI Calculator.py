import os
os.system("cls")

class BodyMassIndex():
    def __init__(self, wgt, hgt):
        self.weight = wgt
        self.height = hgt

    def getBMI(self):
        return self.weight/(self.height**2)

    def getBMICategory(self):
        if self.getBMI() < 15:
            cat = "Starvation"
        elif self.getBMI() < 18.5:
            cat = "Underweight"
        elif self.getBMI() < 25:
            cat = "Normal"
        elif self.getBMI() < 30:
            cat = "Overweight"
        elif self.getBMI() < 40:
            cat = "Obese"
        else:
            cat = "Morbidly Obese"
        return cat

    def showBMIDetails(self): 
        cat = self.getBMICategory()
        bmi = self.getBMI()
        print("\nBMI Category:",cat) 
        if bmi < 18.5 or bmi >= 25:
            ideal_wgt = 21.75*(self.height**2)
            print("Ideal weight:", round(ideal_wgt, 2),"kgs\n")

print("To calculate BMI using weight and height: ")
wgt = float(input("Enter the weight (in Kgs): "))
hgt = float(input("Enter the height (in mts): "))
obj = BodyMassIndex(wgt, hgt)
obj.showBMIDetails()