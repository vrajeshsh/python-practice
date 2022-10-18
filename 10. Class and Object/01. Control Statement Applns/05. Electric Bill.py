import os
os.system("cls")

class ElectricBill():
    def __init__(self):
        self.name = ""
        self.units = 0

    def accept(self):
        self.name = input("Enter the name: ")
        self.units = int(input("Enter the no. of units consumed: "))

    def calculate(self):
        if self.units <= 100:
            bill = 2 * self.units
        elif self.units <= 300:
            bill = (2*100) + 3 * (self.units-100)
        else:
            bill = (2*100) + (3*200) + 5 * (self.units-300)
            bill+= (2.5/100)*bill
        return bill

    def print(self):
        print("\nName of the customer: ", self.name,
        "\nNumber of unit consumed: ", self.units,
        "\nBill Amount: Rs ",round(self.calculate(),2),"\n", sep='')

print("To calculate the electricity bill:")
obj = ElectricBill()
obj.accept()
obj.print()
