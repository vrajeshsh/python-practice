import os
os.system("cls")

class TaxPayer():
    def __init__(self, pan, name, taxableInc):
        self.pan = pan
        self.name = name
        self.taxableInc = taxableInc

    def calculateTax(self):
        if self.taxableInc <= 50000:
            tax = 0
        elif self.taxableInc <=60000:
            tax = .1 * (self.taxableInc - 50000)
        elif self.taxableInc <=150000:
            tax = .2 * (self.taxableInc - 60000) + 1000
        elif self.taxableInc <=850000:
            tax = .3 * (self.taxableInc - 150000) + 19000
        else:
            tax = .3 * (self.taxableInc - 150000) + 19000 + .1 * self.taxableInc

        return tax
        

    def display(self):
        print("\nPAN NO\t\tNAME\t\tTOTAL ANNUAL INCOME\tTAX\n",self.pan,"\t\t", self.name,"\t",self.taxableInc,"\t", self.calculateTax(),"\n", sep='')

print("To calculate the income tax of a user: ")
pan = input("Enter pan card no.: ")
name = input("Enter name: ")
taxableInc = float(input("Enter the taxable income: Rs."))
obj = TaxPayer(pan, name, taxableInc)
obj.display()