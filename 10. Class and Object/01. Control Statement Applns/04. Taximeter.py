import os
os.system("cls")

class Taximeter:
    def __init__(self):
        self.taxino =""
        self.name = ""
        self.kms = 0

    def input(self):
        self.taxino = input("Enter the Taxi Number: ")
        self.name = input("Enter the name: ")
        self.kms = int(input("Enter the number of kilometers travelled: "))

    def calculate(self):
        if self.kms <= 1:
            fare = 25
        elif self.kms <= 6:
            fare = 25 + 10 * (self.kms - 1)
        elif self.kms <= 12:
            fare = 25 + (10 * 5) + 15 * (self.kms - 6)
        elif self.kms<=18:
            fare = 25 + (10 * 5) + (15 * 6) + 20 * (self.kms - 12)
        else:
            fare = 25 + (10 * 5) + (15 * 6) + (20 * 6) + 25 * (self.kms - 18)
        return fare

    def display(self):
        print("\nTaxi No.\tName\t\t\tKilometers travelled\tBill Amount(Rs.)\n",
        self.taxino,"\t\t",self.name,"\t\t",self.kms,"\t\t\t",self.calculate(),"\n",sep='')


print("To calculate the fare of a Taxi ride:")
obj= Taximeter()
obj.input()
obj.display()