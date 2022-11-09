import os
os.system("cls")


class TeleBill():
    def __init__(self, phno, name, n):
        self.phno = phno
        self.name = name
        self.n = n
        self.amt = 0

    def compute(self):
        if self.n>300:
            return (self.n - 300) * 1.5 + 500
        elif self.n > 200:
            return (self.n - 200) * 1.2 + 500
        elif self.n > 100:
            return (self.n - 100) + 500
        else:
            return 500

    def display(self):
        self.amt = self.compute()
        print("\nPHONE NO.\t\tNAME\t\t\tCALLS\tAMOUNT(Rs.)\n",self.phno,
        "\t\t",self.name,"\t\t",self.n,"\t", self.amt,"\n", sep='')


print("To calculate monthly telephone bill of a customer:")
phno = input("ENter the phone number: ")
name = input("Enter the name: ")
n = int(input("Enter number of calls made: "))
obj = TeleBill(phno, name, n)
obj.display()